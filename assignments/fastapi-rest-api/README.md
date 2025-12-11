# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Nesta tarefa, você aprenderá a criar uma API REST completa usando o framework FastAPI do Python. Você construirá uma API de gerenciamento de tarefas (To-Do List) com operações CRUD (Create, Read, Update, Delete) e documentação automática.

## 📝 Tasks

### 🛠️	Criar Endpoints Básicos da API

#### Description
Crie uma API REST com endpoints básicos para gerenciar uma lista de tarefas. A API deve permitir criar, listar, atualizar e deletar tarefas usando o framework FastAPI.

#### Requirements
Completed program should:

- Definir um modelo Pydantic para representar uma tarefa com campos: id, title, description, completed (boolean)
- Implementar endpoint GET `/tasks` para listar todas as tarefas
- Implementar endpoint GET `/tasks/{task_id}` para buscar uma tarefa específica por ID
- Implementar endpoint POST `/tasks` para criar uma nova tarefa
- Implementar endpoint PUT `/tasks/{task_id}` para atualizar uma tarefa existente
- Implementar endpoint DELETE `/tasks/{task_id}` para deletar uma tarefa
- Usar armazenamento em memória (lista ou dicionário) para as tarefas


### 🛠️	Adicionar Validações e Tratamento de Erros

#### Description
Aprimore sua API adicionando validações adequadas nos dados de entrada e tratamento de erros para casos como tarefas não encontradas ou dados inválidos.

#### Requirements
Completed program should:

- Validar que o título da tarefa não está vazio e tem no mínimo 3 caracteres
- Retornar código de status HTTP 404 quando uma tarefa não for encontrada
- Retornar código de status HTTP 400 para dados de entrada inválidos
- Incluir mensagens de erro descritivas nas respostas
- Usar os tipos de resposta apropriados do FastAPI (HTTPException)
- Testar os endpoints usando a documentação automática do Swagger UI (disponível em `/docs`)
