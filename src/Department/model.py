from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.utils.db import Base

class Department(Base):
    __tablename__ = "department"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String, index=True)
    employee_count = Column(Integer, index=True)

    
    employees = relationship("Employee", back_populates="department")