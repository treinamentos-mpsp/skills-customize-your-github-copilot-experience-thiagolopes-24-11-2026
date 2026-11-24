from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Task Tracker API")


class TaskInput(BaseModel):
    title: str = Field(min_length=1)
    description: str = ""
    completed: bool = False


class Task(TaskInput):
    id: int


tasks: dict[int, Task] = {
    1: Task(id=1, title="Read the API assignment", description="Practice GET requests"),
    2: Task(id=2, title="Build a FastAPI route", description="Return a JSON response"),
}


@app.get("/")
def read_root():
    return {"message": "Task Tracker API is running"}


# TODO: Add GET /tasks and GET /tasks/{task_id}.
# TODO: Add POST /tasks and return the created task with HTTP 201.
# TODO: Add PUT /tasks/{task_id} and DELETE /tasks/{task_id}.
# TODO: Add an optional `completed` query parameter to GET /tasks.