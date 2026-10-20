from pydantic_core.core_schema import bool_schema
from fastapi import HTTPException, status, Request
from src.Employee.dtos import EmployeeBase,EmployeeResponseSchema
from sqlalchemy.orm import Session
from src.Employee.model import Employee
from datetime import date


def create_employee(body:EmployeeBase, db:Session):
    db_emp=Employee(
        name=body.name,
        age=body.age,
        salary=body.salary,
        doj=body.doj,
        department_id=body.department_id
    )

    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp

def get_all_employee(db:Session, page:int=1, limit: int = 5 ):
    start=(page-1) * limit
    total=db.query(Employee).count()
    employees=db.query(Employee).offset(start).limit(limit).all()
    return {
        "page":page,
        "limit": limit,
        "total":total,
        "employees":employees
    }

def get_by_id(id:int, db:Session):
    user=db.query(Employee).filter(Employee.id==id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return user

def get_by_deptid(dept_id:int, db:Session):
    dept= db.query(Employee).filter(Employee.department_id==dept_id).all()
    if not dept:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Department not found")
    

    return dept

def get_by_doj(doj:date, db:Session, page:int=1,limit:int=5):
    start= (page-1)  * limit
    total=db.query(Employee).filter(Employee.doj==doj).count()
    user=db.query(Employee).filter(Employee.doj==doj).offset(start).limit(limit).all()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return {
        "page":page,
        "limit":limit,
        "total":total,
        "employees":user
    }   

def update_user(id:int,body:EmployeeBase,db:Session):
    employee=db.query(Employee).filter(Employee.id==id).first() 
    if employee is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    
    updated_data=body.model_dump()
    for field, value in updated_data.items():
        setattr(employee, field,value)
    
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

def delete_employee(id:int, db:Session):
    employee=db.query(Employee).filter(Employee.id==id).first()
    if employee is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Employee not found")
    db.delete(employee)
    db.commit()
    return {"message": "Employee deleted successfully"}
    

    
    




    
    
    




    