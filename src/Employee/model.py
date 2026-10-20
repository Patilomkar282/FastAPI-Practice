from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from src.utils.db import Base
from datetime import date


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer, index=True)
    salary = Column(Integer, index=True)
    doj = Column(Date, default=date.today)

    
    department_id = Column(
        Integer,
        ForeignKey("department.id"),
        index=True
    )

    department = relationship("Department", back_populates="employees")
    user = relationship("User", back_populates="employee", uselist=False)
