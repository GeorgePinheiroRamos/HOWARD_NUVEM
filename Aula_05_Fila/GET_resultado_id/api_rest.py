import logging
from time import perf_counter

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import fila
from modelo import carregar_modelo

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("api-rest")

app = FastAPI(title="API de sentimento com fila", version="2.0.0")
# O modelo é carregado uma vez por processo, nunca por requisição.
modelo = carregar_modelo()


class Entrada(BaseModel):
    texto: str


@app.get("/saude")
def saude():
    inicio = perf_counter()
    resposta = {"status": "ok", "modelo_carregado": modelo is not None}
    logger.info("request id=saude entrada=0 tempo_ms=%.2f", (perf_counter() - inicio) * 1000)
    return resposta


@app.post("/predict-sync")
def predict_sync(entrada: Entrada):
    if not entrada.texto.strip():
        raise HTTPException(status_code=400, detail="O texto não pode ficar vazio.")
    inicio = perf_counter()
    resultado = modelo.prever(entrada.texto)
    resultado["tempo_ms"] = round((perf_counter() - inicio) * 1000, 2)
    logger.info("request id=sync entrada=%d tempo_ms=%.2f", len(entrada.texto), (perf_counter() - inicio) * 1000)
    return resultado


@app.post("/predict", status_code=202)
def predict(entrada: Entrada):
    if not entrada.texto.strip():
        raise HTTPException(status_code=400, detail="O texto não pode ficar vazio.")
    inicio = perf_counter()
    tarefa_id = fila.enfileirar(entrada.texto)
    tempo_ms = round((perf_counter() - inicio) * 1000, 2)
    logger.info("request id=%s entrada=%d tempo_ms=%.2f status=na_fila", tarefa_id, len(entrada.texto), tempo_ms)
    return {"id": tarefa_id, "status": "na_fila"}


@app.get("/resultado/{tarefa_id}")
def resultado(tarefa_id: str):
    inicio = perf_counter()
    dados = fila.buscar_resultado(tarefa_id)
    tempo_ms = round((perf_counter() - inicio) * 1000, 2)
    if dados is None:
        logger.info("request id=%s entrada=0 tempo_ms=%.2f status=nao_encontrado", tarefa_id, tempo_ms)
        raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
    logger.info("request id=%s entrada=0 tempo_ms=%.2f status=%s", tarefa_id, tempo_ms, dados.get("status"))
    return dados
