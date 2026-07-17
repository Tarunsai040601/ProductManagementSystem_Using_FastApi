from pydantic import BaseModel
class UserSchems(BaseModel):
    name:str
    email:str
    password:str


class loginScheam(BaseModel):
    email:str
    password:str