import logging
from concurrent import futures
from time import perf_counter

import grpc

from modelo import carregar_modelo
import inferencia_pb2
import inferencia_pb2_grpc

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("grpc")


class ServicoInferencia(inferencia_pb2_grpc.InferenciaServicer):
    def __init__(self):
        self.modelo = carregar_modelo()
        logger.info("modelo carregado")

    def _resposta(self, texto):
        r = self.modelo.prever(texto)
        return inferencia_pb2.RespostaPrever(
            texto=r["texto"], sentimento=r["sentimento"], confianca=r["confianca"]
        )

    def Prever(self, request, context):
        inicio = perf_counter()
        resposta = self._resposta(request.texto)
        logger.info("id=grpc-prever entrada=%d tempo_ms=%.2f", len(request.texto), (perf_counter() - inicio) * 1000)
        return resposta

    def PreverLote(self, request, context):
        inicio = perf_counter()
        resposta = inferencia_pb2.RespostaLote(
            resultados=[self._resposta(texto) for texto in request.textos]
        )
        logger.info("id=grpc-lote entrada=%d itens tempo_ms=%.2f", len(request.textos), (perf_counter() - inicio) * 1000)
        return resposta


def servir(porta: int = 50051):
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inferencia_pb2_grpc.add_InferenciaServicer_to_server(ServicoInferencia(), servidor)
    servidor.add_insecure_port(f"[::]:{porta}")
    servidor.start()
    logger.info("escutando na porta %d", porta)
    servidor.wait_for_termination()


if __name__ == "__main__":
    servir()
