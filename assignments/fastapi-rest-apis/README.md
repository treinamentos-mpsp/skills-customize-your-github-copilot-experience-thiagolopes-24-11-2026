# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para gerenciar tarefas usando FastAPI. Você vai praticar rotas HTTP, parâmetros, validação de dados com modelos Pydantic e respostas apropriadas para cada operação.

## 📝 Tasks

### 🛠️ Create Read Endpoints

#### Description
Implemente endpoints para listar as tarefas disponíveis e buscar uma tarefa pelo seu identificador. Use o conjunto de dados em memória do starter code.

#### Requirements
Sua API deve:

- Responder a `GET /tasks` com a lista de tarefas
- Responder a `GET /tasks/{task_id}` com a tarefa correspondente
- Retornar HTTP `404` quando o identificador não existir

### 🛠️ Add Tasks with Validated Data

#### Description
Crie um endpoint para adicionar uma tarefa. Defina um modelo Pydantic para os dados recebidos e deixe o FastAPI validar o corpo da requisição.

#### Requirements
Sua API deve:

- Responder a `POST /tasks` usando um modelo Pydantic para o corpo
- Exigir um título não vazio e aceitar uma descrição opcional
- Gerar um identificador único e retornar a tarefa criada com HTTP `201`

### 🛠️ Update and Delete Tasks

#### Description
Adicione operações para atualizar e remover tarefas existentes. Mantenha os dados em memória durante a execução do servidor.

#### Requirements
Sua API deve:

- Responder a `PUT /tasks/{task_id}` para atualizar os dados de uma tarefa existente
- Responder a `DELETE /tasks/{task_id}` para remover uma tarefa existente
- Retornar HTTP `404` quando uma operação usar um identificador inexistente
- Retornar HTTP `204` após remover uma tarefa, sem corpo de resposta

### 🛠️ Filter and Explore the API

#### Description
Adicione um parâmetro de consulta para filtrar tarefas pelo estado de conclusão e confira a documentação interativa gerada pelo FastAPI.

#### Requirements
Sua API deve:

- Aceitar `completed` como parâmetro opcional em `GET /tasks`
- Retornar apenas tarefas que correspondam ao filtro, quando ele for informado
- Continuar retornando todas as tarefas quando o filtro não for informado
- Iniciar com Uvicorn e permitir testar as rotas em `/docs`