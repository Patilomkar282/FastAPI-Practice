from pydantic import BaseModel
from datetime import date

class EmployeeBase(BaseModel):
    name:str
    age:int
    salary:int
    doj:date
    department_id:int

class EmployeeResponseSchema(BaseModel):
    id: int | None = None
    name: str
    age: int
    salary: int
    doj: date
    department_id: int

    class Config:
        from_attributes = True
    
class PageinatedEmplyeesResponse(BaseModel):
    page:int
    limit:int
    total:int
    employees:list[EmployeeResponseSchema]


    
    