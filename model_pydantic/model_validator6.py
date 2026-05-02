from pydantic import BaseModel,EmailStr,AnyUrl,Field,model_validator
from typing import List,Dict,Optional,Annotated

from fastapi import FastAPI
app = FastAPI()

#define pydantic
class Patient(BaseModel):
    name:str
    email: EmailStr
    age:int
    contact: Dict[str, str]


    @model_validator(mode='after')
    def emergency_contact_validator(cls,model):
        if model.age>60 and 'emergency' not in model.contact:
            raise ValueError('Patient Older than 60 must have emergency conatct Number')
        return model

#function
def insert_patient_data(patient:Patient):
    print("Patient inserted successfully")
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.contact)
    print("\n")

#raw data
patient_info1={
  "name": "Ankita Sharma",
  'email':'abcankita@hdfc.com',
  "age": 24,  #wont show error as age less than 60
  "contact": {
    "phone": "9876543210",
    "city": "Delhi"
  }
}

patient_info2={
  "name": "Abhay Sharma",
  'email':'abcabhay@gmail.com',
  "age": 60,  #can show error as age greater than 60 if we dont add emergency in contact
  "contact": {
    "emergency": "9876543210",
    "city": "Delhi"
  }
}
#make pydantic object 1 for first patient
patient1=Patient(**patient_info1)

#make pydantic object 2 for second patient
patient2=Patient(**patient_info2)

#pass object1 to function
insert_patient_data(patient1)

#pass object2 to function
insert_patient_data(patient2)
