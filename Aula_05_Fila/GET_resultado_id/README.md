# GET /resultado/{id}

Esta atividade consulta o estado de uma tarefa criada por `POST /predict`. Enquanto o worker não termina, a API informa o estado atual; quando a tarefa fica pronta, devolve o resultado. Um identificador inexistente retorna `404`.

O recorte do código está em [`api_rest.py`](./api_rest.py). Os componentes compartilhados permanecem na raiz da Aula 08.

Para executar, siga o [README principal da Aula 08](../README.md) e inicie a API pela raiz:

```bash
cd Aula_08_Fila
uvicorn api_rest:app --host 0.0.0.0 --port 8000
```

Exemplo:

```bash
curl http://localhost:8000/resultado/ID_DA_TAREFA
```
