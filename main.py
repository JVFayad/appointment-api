from typing import Optional
from xmlrpc.client import DateTime

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Appointment(BaseModel):
    title: str 
    description: str
    minutes: int
    remote: Optional[bool] = None


@app.get("/")
async def read_root():
    return "Welcome to the Appointments API!"


@app.get("/appointments/{appointment_id}")
async def read_appointment(appointment_id: int, q: Optional[str] = None):
    return {"appointment_id": appointment_id, "q": q}


@app.put("/appointments/{appointment_id}")
async def update_appointment(appointment_id: int, appointment: Appointment):
    return {
        "appointment_title": appointment.title,
        "appointment_id": appointment_id
    }