from pydantic import BaseModel
class UserSchems(BaseModel):
    email:str
    password:str