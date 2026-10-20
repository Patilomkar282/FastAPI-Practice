from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.utils.db import Base

class User(Base):
    __tablename__ = "usersdetails"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="EMPLOYEE", index=True)  
    is_active = Column(Boolean, default=True)

    
    employee_id = Column(Integer, ForeignKey("employees.id"), unique=True, nullable=True, index=True)

   
    employee = relationship("Employee", back_populates="user")
