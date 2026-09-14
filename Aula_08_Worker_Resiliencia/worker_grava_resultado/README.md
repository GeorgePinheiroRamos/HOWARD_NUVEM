# worker grava resultado

Esta atividade executa o processamento fora da API. O worker retira a tarefa do Redis, chama o modelo carregado na inicialização e grava o resultado para que `GET /resultado/{id}` possa consultá-lo.

O recorte do código está em [`worker.py`](./worker.py), com o cliente de teste em [`cliente_fila.py`](./cliente_fila.py). O tratamento de falhas faz até três tentativas e envia tarefas persistentes com erro para a fila `tarefas:dead-letter`.

Para executar, siga o [README principal da Aula 08](../README.md), suba o Redis e inicie o worker a partir da raiz:

```bash
cd Aula_08_Fila
python worker.py
```

Teste o fluxo completo com:

```bash
python cliente_fila.py "o atendimento foi excelente e muito rapido"
```
