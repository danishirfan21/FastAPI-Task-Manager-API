from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db, get_current_user
from app.crud.task import get_tasks, create_task, get_task, update_task, delete_task
from app.schemas.task import TaskCreate, TaskUpdate, TaskInDB
from app.schemas.user import UserInDB

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/", response_model=list[TaskInDB])
async def read_tasks(
    db: AsyncSession = Depends(get_db),
    current_user: UserInDB = Depends(get_current_user),
):
    return await get_tasks(db, user_id=current_user.id)

@router.post("/", response_model=TaskInDB)
async def create_new_task(
    task: TaskCreate,
    db: AsyncSession = Depends(get_db),
    current_user: UserInDB = Depends(get_current_user),
):
    return await create_task(db, task=task, user_id=current_user.id)

@router.get("/{task_id}", response_model=TaskInDB)
async def read_task(
    task_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: UserInDB = Depends(get_current_user),
):
    db_task = await get_task(db, task_id=task_id)
    if not db_task or db_task.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.put("/{task_id}", response_model=TaskInDB)
async def update_existing_task(
    task_id: int,
    task: TaskUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: UserInDB = Depends(get_current_user),
):
    db_task = await get_task(db, task_id=task_id)
    if not db_task or db_task.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Task not found")
    return await update_task(db, task_id=task_id, task=task)

@router.delete("/{task_id}", response_model=TaskInDB)
async def delete_existing_task(
    task_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: UserInDB = Depends(get_current_user),
):
    db_task = await get_task(db, task_id=task_id)
    if not db_task or db_task.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Task not found")
    return await delete_task(db, task_id=task_id)
