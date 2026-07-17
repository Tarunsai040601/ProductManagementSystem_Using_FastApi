from pydantic import BaseModel
class TaskSchema(BaseModel):
    ProductTitle:str
    description:str
    Price:str
    Comments:str

