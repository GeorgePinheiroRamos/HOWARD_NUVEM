# Sistemas Distribuídos — C1.A2

Esta pasta contém a implementação de inferência distribuída com REST, Redis, worker e gRPC. O modelo de sentimento é apenas um componente local.

## Arquitetura

A solução é decomposta em três responsabilidades independentes:

1. **API REST (`api_rest.py`)** recebe requisições FastAPI. `POST /predict` valida a entrada, publica uma tarefa no Redis e devolve `202` com um identificador, sem esperar a inferência. `GET /resultado/{id}` consulta o estado ou o resultado.
2. **Mensageria (`fila.py` + Redis)** transporta tarefas, registra estados e mantém a fila `tarefas:dead-letter` para mensagens que esgotaram as tentativas.
3. **Worker (`worker.py`)** consome a fila, carrega o modelo uma vez por processo, executa a inferência e grava o resultado no Redis. Em falhas, reprocessa até três vezes e depois envia a tarefa para dead-letter.
4. **Serviço gRPC (`servidor_grpc.py`)** expõe `Prever` e `PreverLote` pelo contrato `inferencia.proto`, permitindo comunicação síncrona individual e em lote.

Fluxo assíncrono:

```text
Cliente -> REST /predict -> Redis (tarefas) -> Worker -> modelo -> Redis (resultado)
                                                     |-- falha x3 -> dead-letter
Cliente -> REST /resultado/{id} ---------------------^
```

Todos os serviços registram identificador, tamanho da entrada e tempo de atendimento. O modelo é carregado uma única vez na inicialização de cada processo, nunca dentro de uma requisição.

## Execução do zero

Requisitos: Python 3.11+, Docker e Docker Compose.

```bash
cd Aula_08_Fila
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. inferencia.proto
```

Em um terminal, suba a mensageria:

```bash
docker compose up -d
```

Em outro terminal, inicie a API REST:

```bash
source .venv/bin/activate
uvicorn api_rest:app --host 0.0.0.0 --port 8000
```

Em um terceiro terminal, inicie o worker:

```bash
source .venv/bin/activate
python worker.py
```

A documentação OpenAPI fica em <http://localhost:8000/docs>.

## Testes rápidos

Inferência síncrona:

```bash
curl -X POST http://localhost:8000/predict-sync \\
  -H 'Content-Type: application/json' \\
  -d '{"texto":"o atendimento foi excelente"}'
```

Inferência assíncrona e consulta:

```bash
python cliente_fila.py "o atendimento foi excelente e muito rapido"
```

Ou manualmente:

```bash
curl -i -X POST http://localhost:8000/predict \\
  -H 'Content-Type: application/json' \\
  -d '{"texto":"a entrega foi muito boa"}'
# use o id retornado:
curl http://localhost:8000/resultado/ID_DA_TAREFA
```

Para iniciar o gRPC:

```bash
python servidor_grpc.py
```

O método `PreverLote` recebe vários textos no mesmo pedido e devolve uma resposta para cada item. O contrato está em `inferencia.proto`; os arquivos `inferencia_pb2.py` e `inferencia_pb2_grpc.py` são gerados pelo comando acima e não devem ser editados manualmente.

## Resiliência

O worker incrementa `tentativa` antes de processar. Exceções são capturadas para que o processo continue atendendo outras mensagens. Até duas falhas causam reencaminhamento à fila principal; a terceira falha grava o estado `falhou` no resultado e publica a mensagem completa, incluindo o erro, em `tarefas:dead-letter`.

Para inspecionar a fila de descarte:

```bash
docker compose exec redis redis-cli LLEN tarefas:dead-letter
docker compose exec redis redis-cli LRANGE tarefas:dead-letter 0 -1
```

## Critérios atendidos

| Critério | Evidência |
|---|---|
| Arquitetura e decomposição | API REST, worker, Redis e serviço gRPC separados |
| Comunicação | REST síncrono/assíncrono, Redis e gRPC individual/em lote |
| Resiliência | retentativas, captura de exceções e dead-letter após 3 tentativas |
| Execução reproduzível | `requirements.txt`, `docker-compose.yml`, contrato `.proto` e este README |

Para encerrar a infraestrutura:

```bash
docker compose down
```
