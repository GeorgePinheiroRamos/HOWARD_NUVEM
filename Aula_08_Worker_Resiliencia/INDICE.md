# Sistemas Distribuídos — C1.A2

A [documentação principal](./README.md) explica a arquitetura e a execução completa.

| Atividade | Arquivos da atividade |
|---|---|
| [`POST_predict/`](./POST_predict/) | `README.md`, `api_rest.py` — submissão assíncrona pelo `POST /predict` |
| [`GET_resultado_id/`](./GET_resultado_id/) | `README.md`, `api_rest.py` — consulta pelo `GET /resultado/{id}` |
| [`worker_grava_resultado/`](./worker_grava_resultado/) | `README.md`, `worker.py`, `cliente_fila.py` — processamento e gravação do resultado |

Os componentes compartilhados permanecem na raiz da Aula 08 para permitir a execução integrada: `fila.py`, `modelo.py`, `docker-compose.yml`, `requirements.txt`, o contrato gRPC e os stubs gerados. As cópias de código dentro das atividades representam o recorte de cada exercício.
