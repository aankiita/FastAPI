from pydantic import BaseModel
from typing import Literal

from fastapi import FastAPI
app = FastAPI()

#define pydantic
class Patient(BaseModel):
    name:str
    city:str
    age:int
    gender: Literal['male', 'female', 'others']
    height:float
    weight: float


#function
def insert_patient_data(patient:Patient):
    print("Patient inserted successfully ✅")
    print(patient.name)
    print(patient.age)
    print(patient.city)
    print(patient.height)
    print(patient.gender)
    print(patient.weight)


#raw data
patient_info={"name": "Ankita Sharma", "city": "Delhi", "age": 28, "gender": "female", "height": 1.65, "weight": 90.0}

#make pydantic object
patient1=Patient(**patient_info)

#pass object to function
insert_patient_data(patient1)
