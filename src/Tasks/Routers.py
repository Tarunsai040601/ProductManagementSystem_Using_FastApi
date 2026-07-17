from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.Tasks import Controllers
from src.Tasks.dtos import TaskSchema
from src.Utils.db import get_db
from src.Utils.helper import Authtoken
from src.Users.Models import UserModel

TaskRouter = APIRouter(prefix="/task")

# get all data
@TaskRouter.get("/")
def getData(db=Depends(get_db),user:UserModel=Depends(Authtoken)):
    return Controllers.get_controller(db)

# post data
@TaskRouter.post("/create")
def createData(body: TaskSchema, db: Session = Depends(get_db),user:UserModel=Depends(Authtoken)):
    return Controllers.createController(body, db)

# get by id
@TaskRouter.get("/get/{task_id}")
def get_data(task_id:int,db=Depends(get_db),user:UserModel=Depends(Authtoken)):
    return Controllers.getDataId(task_id,db)

# updated
@TaskRouter.put("/updated/{task_id}")
def updatedData(body:TaskSchema,task_id:int,db=Depends(get_db),user:UserModel=Depends(Authtoken)):
    return Controllers.updatedTask(body,task_id,db)


# delete
@TaskRouter.delete("/delete/{task_id}")
def updatedData(task_id:int,db=Depends(get_db),user:UserModel=Depends(Authtoken)):
    return Controllers.DeletedTask(task_id,db)


