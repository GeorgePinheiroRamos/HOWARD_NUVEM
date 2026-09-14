# Aula 6 — Resiliência

Esta aula concentra o tratamento de falhas da aplicação distribuída: novas tentativas, estados de processamento, mensagens em dead-letter e recuperação após indisponibilidade do Redis.

## Arquivos

- `fila.py`: estados, tentativas e fila de descarte.
- `docker-compose.yml`: Redis com volume e healthcheck.
- `requirements.txt`: dependências reproduzíveis.

A implementação completa do worker está na [Aula 8 — Worker e resiliência](../Aula_08_Worker_Resiliencia/README.md).
