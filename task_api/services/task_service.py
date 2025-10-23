
from sqlalchemy.orm import Session
from ..models import task as task_model
from ..models import task_schema

def get_task(db: Session, task_id: int):
    return db.query(task_model.Task).filter(task_model.Task.id == task_id).first()

def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(task_model.Task).offset(skip).limit(limit).all()

def create_task(db: Session, task: task_schema.TaskCreate):
    db_task = task_model.Task(title=task.title, description=task.description, completed=task.completed)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, task: task_schema.TaskCreate):
    db_task = db.query(task_model.Task).filter(task_model.Task.id == task_id).first()
    if db_task:
        db_task.title = task.title
        db_task.description = task.description
        db_task.completed = task.completed
        db.commit()
        db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int):
    db_task = db.query(task_model.Task).filter(task_model.Task.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task
