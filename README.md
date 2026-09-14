# Sistemas Distribuídos — C1.A2

Bem-vindo ao repositório de atividades da disciplina. O conteúdo está separado por aula para que cada exercício tenha sua própria página, relatório e código. A implementação com fila está na [Aula 08 — Fila](./Aula_08_Fila/README.md).

## Navegação por aula

| Aula ou módulo | Tema | Página |
|---|---|---|
| Aula 1 | Comunicação TCP/UDP e servidor de eco | [`Aula1/`](./Aula1/README.md) |
| Aula 4 | Contratos e stubs gRPC | [`Aula_04_gRPC/`](./Aula_04_gRPC/README.md) |
| Aula 5 | API REST e OpenAPI | [`Aula_05_REST/`](./Aula_05_REST/README.md) |
| Aula 6 | IA como serviço | [`Aula_06_IA/`](./Aula_06_IA/README.md) |
| Aula 8 | Fila, worker, resiliência e gRPC em lote | [`Aula_08_Fila/`](./Aula_08_Fila/README.md) · [`Índice`](./Aula_08_Fila/INDICE.md) |
| Threads | Comparação sequencial e concorrente | [`THREADS/`](./THREADS/README.md) |

## Arquitetura

A solução final combina uma API REST FastAPI, um worker independente e Redis como mensageria e armazenamento de estados. A submissão assíncrona retorna `202` com um identificador; o worker executa o modelo carregado uma vez por processo e grava o resultado para consulta posterior. O mesmo projeto também oferece o serviço gRPC com os métodos `Prever` e `PreverLote`.

O tratamento de falhas inclui captura de exceções, até três tentativas por tarefa e uma fila `tarefas:dead-letter` para mensagens que não puderam ser processadas. Os serviços registram identificador, tamanho da entrada e tempo de resposta. A execução é reproduzível com `requirements.txt`, Docker Compose, contrato Protocol Buffers e instruções passo a passo no README da Aula 08.

## Como começar

Para estudar uma aula específica, entre na pasta indicada na tabela e leia o README antes de executar os scripts. Para avaliar a entrega, siga diretamente o [guia completo da Aula 08](./Aula_08_Fila/README.md), que contém instalação, inicialização do Redis, execução da API e do worker, testes REST e inicialização do gRPC.

## Autoria

Os nomes e os commits existentes da equipe foram preservados. Esta organização não adiciona colaborador, conta, assinatura ou coautoria externa ao repositório.
