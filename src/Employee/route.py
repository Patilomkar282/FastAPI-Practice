from fastapi import APIRouter, Depends, status, Request
from sqlalchemy.orm import Session
from src.utils.db import get_db
import src.Employee.dtos as dtos
import src.Employee.controller as controller
from src.Employee.dtos import EmployeeBase,EmployeeResponseSchema, PageinatedEmplyeesResponse
from datetime import date

employeeroutes=APIRouter()

@employeeroutes.post("/create", status_code=status.HTTP_201_CREATED, response_model=EmployeeResponseSchema)
def create_employee(body:EmployeeBase , db:Session=Depends(get_db)):
    return controller.create_employee(body,db)

@employeeroutes.get("/getall", status_code=status.HTTP_200_OK, response_model=PageinatedEmplyeesResponse)
def get_all_employee(db:Session=Depends(get_db), page:int=1, limit:int=5):
    return controller.get_all_employee(db,page,limit)

@employeeroutes.get("/getbyid", status_code=status.HTTP_200_OK, response_model=EmployeeResponseSchema)
def get_by_id(id:int, db:Session=Depends(get_db)):
    return controller.get_by_id(id,db)

@employeeroutes.get("/getbydept", status_code=status.HTTP_200_OK, response_model=list[EmployeeResponseSchema])
def get_by_dept(dept_id:int, db:Session=Depends(get_db)):
    return controller.get_by_deptid(dept_id,db)

@employeeroutes.get("/getbydoj", status_code=status.HTTP_200_OK,response_model=PageinatedEmplyeesResponse)
def get_by_doj(doj:date, db:Session=Depends(get_db), page:int =1, limit:int= 5):
    return controller.get_by_doj(doj,db, page, limit)

@employeeroutes.put("/update/{id}", status_code=status.HTTP_200_OK, response_model=EmployeeResponseSchema)
def update_user(id:int,body:EmployeeBase, db:Session=Depends(get_db)):
    return controller.update_user(id,body,db)

@employeeroutes.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(id:int, db:Session=Depends(get_db)):
    return controller.delete_employee(id,db)

    



