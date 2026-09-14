# Sistemas Distribuídos — C1.A2

A [documentação principal](./README.md) explica a arquitetura e a execução completa.

| Área | Arquivos |
|---|---|
| POST /predict | [`POST_predict/`](./POST_predict/), `api_rest.py` |
| GET /resultado/{id} | [`GET_resultado_id/`](./GET_resultado_id/), `api_rest.py` |
| worker grava resultado | [`worker_grava_resultado/`](./worker_grava_resultado/), `worker.py` |
| Mensageria | `fila.py`, `docker-compose.yml` |
| Worker | `worker.py` |
| gRPC | `inferencia.proto`, `servidor_grpc.py`, stubs gerados |
| Modelo | `modelo.py` |
| Relato | `Relatorio.md` |
| Dependências | `requirements.txt` |

A ordem recomendada para leitura é: arquitetura no README, as três pastas de atividades, contrato `.proto`, fila, worker e relatório.
