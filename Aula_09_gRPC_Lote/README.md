# Aula 9 — gRPC em lote

Esta aula concentra o contrato Protocol Buffers e o serviço gRPC para inferência individual e em lote.

## Arquivos

- `inferencia.proto`: contrato do serviço.
- `servidor_grpc.py`: servidor gRPC.
- `inferencia_pb2.py` e `inferencia_pb2_grpc.py`: stubs gerados.

Para regenerar os stubs:

```bash
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. inferencia.proto
```
