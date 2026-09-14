# POST /predict

Esta atividade recebe um texto pela API REST, cria uma tarefa no Redis e devolve um identificador com status HTTP `202`. A inferência não é executada durante a requisição.

O recorte do código está em [`api_rest.py`](./api_rest.py). Os componentes compartilhados permanecem na raiz da Aula 08 para que o projeto continue executável como um serviço único.

Para executar, siga o [README principal da Aula 08](../README.md) e inicie a API pela raiz:

```bash
cd Aula_08_Fila
uvicorn api_rest:app --host 0.0.0.0 --port 8000
```

Exemplo:

```bash
curl -X POST http://localhost:8000/predict \\
  -H 'Content-Type: application/json' \\
  -d '{"texto":"o atendimento foi excelente"}'
```
