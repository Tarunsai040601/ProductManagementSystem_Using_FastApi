from fastapi import HTTPException,status,Request
from src.Users.dtos import UserSchems
from sqlalchemy.orm import Session
from src.Users.Models import UserModel
from pwdlib import PasswordHash
from datetime import datetime, timedelta
from src.Utils.settings import settings
import jwt


password_hash = PasswordHash.recommended()


def get_password_hash(password):
    return password_hash.hash(password)


def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


# register controller
def registerController(body:UserSchems,db:Session):
    is_User=db.query(UserModel).filter(UserModel.email==body.email).first()
    if is_User:
        raise HTTPException(
        status_code=400,
        detail=f"Email already exists with email: {body.email}"
        )
            
     # Hash password
    hashed_password = get_password_hash(body.password)

    # Create user
    new_user = UserModel(
        email=body.email,
        password=hashed_password
    )

    # Save to database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "data": new_user
    }


# login controller
def loginController(body:UserSchems,db:Session):
    is_User=db.query(UserModel).filter(UserModel.email==body.email).first()
    if not is_User:
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"user not found with {body.email}"
        )
    
    if not verify_password(body.password, is_User.password):
        raise HTTPException(
        status_code=401,
        detail="Invalid password"
    )
    exp_time=datetime.now()+timedelta(settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token=jwt.encode({"id":is_User.id,"email":is_User.email,"exp":exp_time},settings.SECRET_KEY,settings.ALGORITHM)

    return {
    "message": "Login successful",
    "details":is_User.email,
    "access_token": token,
    # "token_type": "bearer"
}


# token send
def Authtoken(request:Request):
    pass