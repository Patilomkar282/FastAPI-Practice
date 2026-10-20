from pydantic import BaseModel

class DepartmentBase(BaseModel):
    name:str
    location:str
    employee_count:int

class DepartmentResponseSchema(BaseModel):
    id: int | None = None
    name: str
    location: str
    employee_count: int

    class Config:
        from_attributes = True

class PaginatedDepartmentResponse(BaseModel):
    page: int
    limit: int
    total: int
    data: list[DepartmentResponseSchema]



