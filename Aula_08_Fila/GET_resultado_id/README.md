# GET /resultado/{id}

Esta atividade consulta o estado de uma tarefa criada por `POST /predict`. Enquanto o worker não termina, a API informa o estado atual; quando a tarefa fica pronta, devolve o resultado. Um identificador inexistente retorna `404`.

A implementação integrada está em [`../api_rest.py`](../api_rest.py), na função `resultado`, usando a consulta compartilhada de [`../fila.py`](../fila.py).

Exemplo:

```bash
curl http://localhost:8000/resultado/ID_DA_TAREFA
```
