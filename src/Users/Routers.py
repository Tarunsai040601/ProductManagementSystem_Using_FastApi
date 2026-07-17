from fastapi import APIRouter,Depends,status,Request
from src.Utils.db import get_db
from src.Users.dtos import UserSchems
from src.Users import Controllers
from sqlalchemy.orm import Session


userRouter=APIRouter(prefix="/auth")


# register router
@userRouter.post("/register",status_code=status.HTTP_201_CREATED)
def register(body:UserSchems,db:Session=Depends(get_db)):
    return Controllers.registerController(body,db)

# login router
@userRouter.post("/login",status_code=status.HTTP_201_CREATED)
def login(body:UserSchems,db:Session=Depends(get_db)):
    return Controllers.loginController(body,db)


# authentication
@userRouter.get("/get",status_code=status.HTTP_200_OK)
def authentication(request:Request,db:Session=Depends(get_db)):
    return Controllers.Authtoken(request,db)