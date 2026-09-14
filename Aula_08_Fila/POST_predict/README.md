# POST /predict

Esta atividade recebe um texto pela API REST, cria uma tarefa no Redis e devolve um identificador com status HTTP `202`. A inferência não é executada durante a requisição.

A implementação integrada está em [`../api_rest.py`](../api_rest.py), na função `predict`. Os componentes compartilhados permanecem na pasta da Aula 08 para que o projeto continue executável como um serviço único: [`../fila.py`](../fila.py), [`../modelo.py`](../modelo.py) e [`../docker-compose.yml`](../docker-compose.yml).

Exemplo:

```bash
curl -X POST http://localhost:8000/predict \\
  -H 'Content-Type: application/json' \\
  -d '{"texto":"o atendimento foi excelente"}'
```
