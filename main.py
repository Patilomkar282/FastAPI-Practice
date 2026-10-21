from fastapi import FastAPI
from src.Employee.route import employeeroutes
from src.Department.route import departmentroutes
from src.Authentication.routes import userrouter
from src.utils.db import engine,Base


Base.metadata.create_all(bind=engine)
app = FastAPI(title="Practice project to understand fast api")
app.include_router(employeeroutes)
app.include_router(departmentroutes)

app.include_router(userrouter)



@app.get("/")
def home():
    return {
        "message": "Hello Home"
    }
