# here i am taken helper.py as middleware for protect route


from fastapi import HTTPException,status,Request,Depends
from sqlalchemy.orm import Session
from src.Utils.settings import settings
from datetime import datetime, timedelta
from src.Users.Models import UserModel
from src.Utils.db import get_db 
import jwt

# token send
def Authtoken(request:Request,db:Session=Depends(get_db)):
    print("request:",request.headers.get("Authorization"))
    auth_header=request.headers.get("Authorization")
    print("token:",auth_header)
    if not auth_header:
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Authorization header is missing"
    )
    token=auth_header.split(" ")[-1]

# here storing the token and secret key also
    data=jwt.decode(token,settings.SECRET_KEY,settings.ALGORITHM)
    print('data:',data)
    user_id=data.get("id")
    exp_data=data.get("exp")

    current_time=datetime.now().timestamp()

    # here comparing exp_time and present time
    if current_time > exp_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="your unauthorized"
            )
    User=db.query(UserModel).filter(UserModel.id==user_id).first()
    if not User:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="your unauthorized"
            )

    
# if  auth token is matched it return the token details
    return({"done:":{"email":User.email,"id":User.id}})