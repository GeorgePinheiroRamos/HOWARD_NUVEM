# Aula 8 — Worker e resiliência

Esta aula executa o processamento fora da API. O worker consome tarefas, executa a inferência, grava o resultado e encaminha mensagens que falharam após as tentativas para a dead-letter queue.

## Arquivos principais

- `worker_grava_resultado/worker.py`: processo consumidor.
- `worker_grava_resultado/cliente_fila.py`: cliente de teste.
- `fila.py`: estados, tentativas e dead-letter.
- `modelo.py`: carregamento do modelo.

## Execução

```bash
cd Aula_08_Worker_Resiliencia
pip install -r requirements.txt
PYTHONPATH=. python -m worker_grava_resultado.worker
```

A atividade de publicação e consulta das tarefas está em [Aula 5 — Fila](../Aula_05_Fila/README.md). A atividade de gRPC em lote está em [Aula 9 — gRPC em lote](../Aula_09_gRPC_Lote/README.md).
