import uvicorn
from fastapi import FastAPI, File, UploadFile, status, Header, Request, Depends
from fastapi.staticfiles import StaticFiles
import schema
app = FastAPI()

@app.get("/addPatient", tags=["Patients"])
async def addPatient(name, gender, address):
    schema.add_new_user(name, gender, address)
    return "lol"

@app.get("/getPatients", tags=["Patients"])
async def getAllPatient():
    t = schema.get_user()
    return t

@app.delete("/deletePatient", tags=["Patients"])
async def deletePatient(id):
    return "lol"

@app.post("/registration", tags=["Login"])
async def registration():
    return "lol"

@app.get("/login", tags=["Login"])
async def login():
    return "lol"

@app.post("/addAppointment", tags=["Appointments"])
async def addAppointment():
    return "lol"

@app.get("/getAppointments", tags=["Appointments"])
async def getAppointments():
    return "lol"