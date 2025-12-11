"""
FastAPI REST API - Starter Code
================================
Complete o código abaixo para criar uma API REST de gerenciamento de tarefas.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Crie a aplicação FastAPI
app = FastAPI(
    title="To-Do List API",
    description="API para gerenciar uma lista de tarefas",
    version="1.0.0"
)

# TODO: Defina o modelo Pydantic para uma Task
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False


# Armazenamento em memória para as tarefas
tasks_db = []
next_id = 1


# TODO: Implemente o endpoint GET /tasks para listar todas as tarefas
@app.get("/")
def read_root():
    """Endpoint raiz da API"""
    return {"message": "Bem-vindo à API de To-Do List"}


# TODO: Implemente o endpoint GET /tasks/{task_id} para buscar uma tarefa específica


# TODO: Implemente o endpoint POST /tasks para criar uma nova tarefa


# TODO: Implemente o endpoint PUT /tasks/{task_id} para atualizar uma tarefa


# TODO: Implemente o endpoint DELETE /tasks/{task_id} para deletar uma tarefa


# Para executar a aplicação:
# 1. Instale o FastAPI e Uvicorn: pip install fastapi uvicorn
# 2. Execute: uvicorn starter-code:app --reload
# 3. Acesse a documentação em: http://localhost:8000/docs
