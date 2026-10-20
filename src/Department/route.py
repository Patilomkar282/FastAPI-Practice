from fastapi import APIRouter, status, Depends 
import src.Department.controller as controller
from src.Department.dtos import DepartmentBase, DepartmentResponseSchema, PaginatedDepartmentResponse
from src.utils.db import get_db
from sqlalchemy.orm import Session

departmentroutes=APIRouter(prefix="/dept", tags=["Department"])

@departmentroutes.post("/createdept", status_code=status.HTTP_201_CREATED, response_model=DepartmentResponseSchema)
def create_dept(body:DepartmentBase, db:Session=Depends(get_db)):
    return controller.create_dept(body,db)


@departmentroutes.get("/getalldept", status_code=status.HTTP_200_OK, response_model=PaginatedDepartmentResponse)
def get_all_dept(page: int = 1, limit: int = 5, db: Session = Depends(get_db)):
    return controller.get_all_dept(db, page=page, limit=limit)

@departmentroutes.get("/getbyid/{dept_id}", status_code=status.HTTP_200_OK,response_model=DepartmentResponseSchema)
def get_dept_by_id(dept_id:int, db:Session=Depends(get_db)):
    return controller.get_dept_by_id(dept_id,db)

@departmentroutes.get("/getbyempcount/{count}", status_code=status.HTTP_200_OK, response_model=list[DepartmentResponseSchema])
def get_by_empcount(count:int, db:Session=Depends(get_db)):
    return controller.get_by_empcount(count,db)

@departmentroutes.put("/updatedept/{id}", status_code=status.HTTP_200_OK, response_model=DepartmentResponseSchema)
def update_dept(id: int, body:DepartmentBase, db:Session=Depends(get_db)):
    return controller.update_dept(id,body,db)

@departmentroutes.delete("/deletedept/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dept(id:int, db:Session=Depends(get_db)):
    return controller.delete_dept(id, db)