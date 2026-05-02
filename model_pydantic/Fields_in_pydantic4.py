from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated


from fastapi import FastAPI
app = FastAPI()

#define pydantic
class Patient(BaseModel):
    name: Annotated[str, Field(min_length=3, max_length=50,
        title="Patient Name",
        description="Give Full name of the patient",
        examples=["Ankita Sharma", "Ravi Kumar"])]
    email: EmailStr
    linkedln_url: AnyUrl
    age:int=Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]#strict=True means if user pass weight as string dont convert it into float just show Error.
    married: Annotated[bool,Field(default=False,description="If the patient is married or not")]
    allergics: Annotated[Optional[List[str]],Field(title="Allergies",max_length=5)]
    contact: Dict[str, str]

#function
def insert_patient_data(patient:Patient):
    print("Patient inserted successfully")
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.linkedln_url)
    print(patient.married)
    print(patient.allergics)
    print(patient.contact)

#raw data
patient_info1={
  "name": "Ankita Sharma",
  "email": "ankita@gmail.com",
  "linkedln_url": "https://www.linkedin.com/in/ankitasharma",
  "age": 28,
  "weight":56.7,
  "married": False,
  "allergics": ["dust", "pollen"],
  "contact": {
    "phone": "9876543210",
    "city": "Delhi"
  }
}
#make pydantic object 1 for first patient
patient1=Patient(**patient_info1)

#pass object1 to function
insert_patient_data(patient1)
