# worker grava resultado

Esta atividade executa o processamento fora da API. O worker retira a tarefa do Redis, chama o modelo carregado na inicialização e grava o resultado para que `GET /resultado/{id}` possa consultá-lo.

A implementação integrada está em [`../worker.py`](../worker.py). O tratamento de falhas faz até três tentativas e envia tarefas persistentes com erro para a fila `tarefas:dead-letter`.

Para executar:

```bash
cd ..
python worker.py
```
