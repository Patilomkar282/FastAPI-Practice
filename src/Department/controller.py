
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.Department.dtos import DepartmentBase, DepartmentResponseSchema
from src.Department.model import Department

def create_dept(body:DepartmentBase, db:Session):
    db_dept=Department(
        name=body.name,
        location=body.location,
        employee_count=body.employee_count

    )

    db.add(db_dept)
    db.commit()
    db.refresh(db_dept)
    return db_dept

def get_all_dept(db:Session, page :int=1, limit:int = 5):
    start= (page-1) * limit
    total= db.query(Department).count()
    departments=db.query(Department).offset(start).limit(limit).all()
    return {
        "page":page,
        "limit":limit,
        "total":total,
        "data":departments
    }

def get_dept_by_id(dept_id:int, db:Session):
    dept=db.query(Department).filter(Department.id==dept_id).first()
    if dept is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Dept not found")
    return dept

def get_by_empcount(count:int, db:Session):
    return db.query(Department).filter(Department.employee_count==count).all()


def update_dept(id:int, body:DepartmentBase, db:Session):
    dept=db.query(Department).filter(Department.id==id).first()
    if dept is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Dept not found")
    
    update_data=body.model_dump()
    for field, value in update_data.items():
        setattr(dept,field,value)

    db.add(dept)
    db.commit()
    db.refresh(dept)
    return dept

def delete_dept(id:int, db:Session):
    dept=db.query(Department).filter(Department.id==id).first()
    if dept is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Dept not found")
    
    db.delete(dept)
    db.commit()

    return {"Message":"Dept deleted successfully"}






