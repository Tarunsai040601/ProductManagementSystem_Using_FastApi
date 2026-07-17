from sqlalchemy.orm import Session
from src.Tasks.dtos import TaskSchema
from src.Tasks.Models import TaskModel
from fastapi import HTTPException

# get data
def get_controller(db:Session):
    task=db.query(TaskModel).all()
    return{"message":"fetched all data","details":task}


# post data
def createController(body: TaskSchema, db: Session):
    data = body.model_dump()

    new_task = TaskModel(
        title=data["title"],
        description=data["description"],
        is_completed=data["is_completed"]
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {
        "status": "Task created successfully",
        "details": new_task
    }


# get data by id
def getDataId(task_id:int,db:Session):
    one_task=db.query(TaskModel).get(task_id)
    if not one_task:
        return HTTPException(404,detail=f"task is not found on id:{task_id}")
    return{"message":"fetch the task based on the id","details":one_task}


# update task
def updatedTask(body:TaskSchema,task_id:int,db:Session):
    one_task=db.query(TaskModel).get(task_id)
    if not one_task:
        return HTTPException(404,detail=f"task is not found on id:{task_id}")
    one_task.title=body.title
    one_task.description=body.description
    one_task.is_completed=body.is_completed

    db.add(one_task)
    db.commit()
    db.refresh(one_task)
    return{"message":"updated sucessfuly","details":one_task}


# delete controller
def DeletedTask(task_id:int,db:Session):
    one_task=db.query(TaskModel).get(task_id)
    if not one_task:
        return HTTPException(404,detail=f"task is not found on id:{task_id}")
    db.delete(one_task)
    db.commit()
    return{"message":"task deleted sucessfully","details":one_task}


    