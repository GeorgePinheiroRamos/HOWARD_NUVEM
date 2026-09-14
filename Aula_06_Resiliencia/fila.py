"""Camada de mensageria Redis: tarefas, resultados e fila de descarte."""
import json
import os
import uuid

import redis

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
FILA_TAREFAS = os.getenv("REDIS_QUEUE", "tarefas")
FILA_DEAD_LETTER = os.getenv("REDIS_DEAD_LETTER", "tarefas:dead-letter")
PREFIXO_RESULTADO = "resultado:"
_cliente = None


def cliente():
    global _cliente
    if _cliente is None:
        _cliente = redis.from_url(REDIS_URL, decode_responses=True)
    return _cliente


def enfileirar(texto: str) -> str:
    tarefa_id = str(uuid.uuid4())
    tarefa = {"id": tarefa_id, "texto": texto, "tentativa": 0}
    cliente().rpush(FILA_TAREFAS, json.dumps(tarefa))
    cliente().set(PREFIXO_RESULTADO + tarefa_id, json.dumps({"status": "na_fila"}))
    return tarefa_id


def proxima_tarefa(timeout: int = 5):
    item = cliente().blpop(FILA_TAREFAS, timeout=timeout)
    return json.loads(item[1]) if item else None


def reencaminhar(tarefa: dict) -> None:
    cliente().rpush(FILA_TAREFAS, json.dumps(tarefa))
    cliente().set(PREFIXO_RESULTADO + tarefa["id"], json.dumps({
        "status": "retentando", "tentativa": tarefa["tentativa"]
    }))


def enviar_dead_letter(tarefa: dict, erro: str) -> None:
    tarefa["erro"] = erro
    cliente().rpush(FILA_DEAD_LETTER, json.dumps(tarefa))
    guardar_resultado(tarefa["id"], {
        "status": "falhou", "tentativas": tarefa["tentativa"], "erro": erro
    })


def guardar_resultado(tarefa_id: str, resultado: dict) -> None:
    cliente().set(PREFIXO_RESULTADO + tarefa_id, json.dumps(resultado))


def buscar_resultado(tarefa_id: str):
    bruto = cliente().get(PREFIXO_RESULTADO + tarefa_id)
    return json.loads(bruto) if bruto else None
