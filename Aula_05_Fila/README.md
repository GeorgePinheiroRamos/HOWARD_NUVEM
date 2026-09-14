# Aula 5 — Fila

Esta página documenta a atividade de mensageria com Redis. A API publica tarefas assíncronas e devolve um identificador para acompanhamento.

## Atividades

- [POST /predict](./POST_predict/README.md)
- [GET /resultado/{id}](./GET_resultado_id/README.md)
- `fila.py`: estados, tentativas e resultados.
- `modelo.py`: modelo usado pelo worker.

## Execução

```bash
cd Aula_05_Fila
pip install -r ../Aula_08_Worker_Resiliencia/requirements.txt
# com o Redis em execução:
PYTHONPATH=. uvicorn POST_predict.api_rest:app --host 0.0.0.0 --port 8000
```

A API expõe `POST /predict` com resposta `202 Accepted` e `GET /resultado/{id}` para consulta do processamento.
