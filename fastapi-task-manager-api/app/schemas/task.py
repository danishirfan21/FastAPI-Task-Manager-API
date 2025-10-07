# Task Pydantic schemas

from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class TaskInDB(TaskBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
