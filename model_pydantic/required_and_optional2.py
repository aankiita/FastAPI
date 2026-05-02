from pydantic import BaseModel
from typing import List,Dict,Optional

from fastapi import FastAPI
app = FastAPI()

#define pydantic
class Patient(BaseModel):
    name:str
    age:int
    married:bool=True  #default value
    allergics:Optional[List[str]]  #optional
    contact:Dict[str,str]

#function
def insert_patient_data(patient:Patient):
    print("Patient inserted successfully")
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.allergics)
    print(patient.contact)


#raw data
patient_info={
  "name": "Ankita Sharma",
  "age": 28,
  "married": False,
  "allergics": ["dust", "pollen"],
  "contact": {
    "phone": "9876543210",
    "email": "ankita@gmail.com"
  }
}

patient_info2={
  "name": "Ravi Kumar",
  "city": "Mumbai",
  "age": 35,
  "allergics":["dust", "pollen"],
  "contact": {
    "phone": "9123456780",
    "email": "ravi@gmail.com"
  }
}

#make pydantic object 1 for first patient
patient1=Patient(**patient_info)

#make pydantic object 2 for second patient
patient2=Patient(**patient_info2)

#pass object1 to function
insert_patient_data(patient1)

#pass object2 to function
insert_patient_data(patient2)
