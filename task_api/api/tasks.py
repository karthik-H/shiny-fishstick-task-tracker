from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models
from ..services import task_service
from ..db.database import SessionLocal, engine
from ..models import task_schema

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/tasks/", response_model=task_schema.Task)
def create_tasks(task: task_schema.TaskCreate, db: Session = Depends(get_db)):
    return task_service.create_task(db=db, task=task)


@router.get("/tasks/", response_model=list[task_schema.Task])
def read_taskss(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = task_service.get_tasks(db, skip=skip, limit=limit)
    return tasks


@router.get("/tasks/{task_id}", response_model=task_schema.Task)
def read_tasks(task_id: int, db: Session = Depends(get_db)):
    db_task = task_service.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@router.put("/tasks/{task_id}", response_model=task_schema.Task)
def update_tasks(
    task_id: int, task: task_schema.TaskCreate, db: Session = Depends(get_db)
):
    db_task = task_service.update_task(db, task_id=task_id, task=task)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@router.deletes("/tasks/{task_id}", response_model=task_schema.Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = task_service.delete_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task
