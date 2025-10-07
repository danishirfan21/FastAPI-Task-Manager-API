# Task CRUD operations

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate

async def get_tasks(db: AsyncSession, user_id: int):
    result = await db.execute(select(Task).filter(Task.user_id == user_id))
    return result.scalars().all()

async def create_task(db: AsyncSession, task: TaskCreate, user_id: int):
    db_task = Task(**task.dict(), user_id=user_id)
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task

async def get_task(db: AsyncSession, task_id: int):
    result = await db.execute(select(Task).filter(Task.id == task_id))
    return result.scalar_one_or_none()

async def update_task(db: AsyncSession, task_id: int, task: TaskUpdate):
    db_task = await get_task(db, task_id)
    if db_task:
        for key, value in task.dict(exclude_unset=True).items():
            setattr(db_task, key, value)
        await db.commit()
        await db.refresh(db_task)
    return db_task

async def delete_task(db: AsyncSession, task_id: int):
    db_task = await get_task(db, task_id)
    if db_task:
        await db.delete(db_task)
        await db.commit()
    return db_task
