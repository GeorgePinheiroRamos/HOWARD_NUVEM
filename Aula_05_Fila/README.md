# Aula 5 — Fila

Esta página documenta a atividade de mensageria com Redis. A API publica tarefas assíncronas e devolve um identificador para acompanhamento.

## Implementação

- [POST /predict](../Aula_08_Fila/POST_predict/README.md)
- [Fila Redis compartilhada](../Aula_08_Fila/fila.py)
- [Composição Docker](../Aula_08_Fila/docker-compose.yml)

A execução completa está documentada no [README da Aula 08](../Aula_08_Fila/README.md).

## Endpoint principal

```http
POST /predict
```

A resposta é `202 Accepted` e contém o identificador da tarefa enfileirada.
