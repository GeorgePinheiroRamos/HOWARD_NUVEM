# Aula 9 — gRPC em lote

Esta aula concentra o contrato Protocol Buffers e o serviço gRPC para inferência individual e em lote.

## Arquivos

- `inferencia.proto`: contrato do serviço.
- `servidor_grpc.py`: servidor gRPC.
- `inferencia_pb2.py` e `inferencia_pb2_grpc.py`: stubs gerados.
- `modelo.py` e `modelo.joblib`: modelo local carregado uma vez pelo servidor.
- `requirements.txt`: dependências de execução.

## Execução

```bash
cd Aula_09_gRPC_Lote
pip install -r requirements.txt
python servidor_grpc.py
```

Para regenerar os stubs:

```bash
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. inferencia.proto
```

O serviço expõe `Prever` e `PreverLote` na porta `50051`.
