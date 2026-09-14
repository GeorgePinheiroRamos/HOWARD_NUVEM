import logging
from time import perf_counter

import fila
from modelo import carregar_modelo

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("worker")
MAX_TENTATIVAS = 3


def main():
    modelo = carregar_modelo()
    logger.info("modelo carregado; aguardando tarefas")
    while True:
        tarefa = fila.proxima_tarefa(timeout=5)
        if tarefa is None:
            continue
        inicio = perf_counter()
        tarefa["tentativa"] = tarefa.get("tentativa", 0) + 1
        try:
            resultado = modelo.prever(tarefa["texto"])
            resultado.update({
                "status": "pronto",
                "tempo_ms": round((perf_counter() - inicio) * 1000, 2),
                "tentativas": tarefa["tentativa"],
            })
            fila.guardar_resultado(tarefa["id"], resultado)
            logger.info("id=%s entrada=%d tempo_ms=%.2f status=pronto", tarefa["id"], len(tarefa["texto"]), resultado["tempo_ms"])
        except Exception as erro:  # uma tarefa defeituosa não derruba o worker
            logger.exception("id=%s tentativa=%d falha", tarefa["id"], tarefa["tentativa"])
            if tarefa["tentativa"] < MAX_TENTATIVAS:
                fila.reencaminhar(tarefa)
            else:
                fila.enviar_dead_letter(tarefa, str(erro))
                logger.error("id=%s enviado para dead-letter após %d tentativas", tarefa["id"], MAX_TENTATIVAS)


if __name__ == "__main__":
    main()
