import os
import Model.Account as acc
from fastapi import FastAPI

app = FastAPI()

students = [
    {
        'name' : 'Suma',
        'branch' : 'CSC',
        'Id' : '001',
        'City' : 'HYD'
    },
    {
        'name' : 'Ramu',
        'branch' : 'AIML',
        'Id' : '002',
        'City' : 'BLR'
    },
    {
        'name' : 'Latha',
        'branch' : 'EEE',
        'Id' : '003',
        'City' : 'DLH'
    }
]
# GET, PUT, POST, DELETE
@app.get("/Home")
def HomeData():
    return {'House' : 'Kheela Nivas'}

@app.get("/getall")
def GetAllStudents():
    return {'Students' : students}

@app.get("/search/{student_Id}")
def SearchStu(student_Id : str):
    try:
        for stu in students:
            if stu["Id"] == student_Id:
                return{'Name': stu['name']}
    except:
        return {"errorcode" : 400, 'errmessage' : ""}