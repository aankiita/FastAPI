from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated

#field_validator-->search something or conver into uppercase or lowercase to any Field

from fastapi import FastAPI
app = FastAPI()

#define pydantic
class Patient(BaseModel):
    name:str
    email: EmailStr
    age:int
    contact: Dict[str, str]


    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domain=['hdfc.com','icic.com']
        domain_name=value.split('@')[-1]

        if domain_name not in valid_domain:
            raise ValueError('Not a valid Domain')
        return value
    

    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()


#function
def insert_patient_data(patient:Patient):
    print("Patient inserted successfully")
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.contact)

#raw data
patient_info1={
  "name": "Ankita Sharma",
  'email':'abcankita@hdfc.com',
  "age": 28,
  "contact": {
    "phone": "9876543210",
    "city": "Delhi"
  }
}
#make pydantic object 1 for first patient
patient1=Patient(**patient_info1)

#pass object1 to function
insert_patient_data(patient1)
