from pydantic import BaseModel,EmailStr,AnyUrl
from typing import List,Dict,Optional

from fastapi import FastAPI
app = FastAPI()

#define pydantic
class Patient(BaseModel):
    name:str
    email:EmailStr
    linkedln_url:AnyUrl
    age:int
    married:bool=True  #default value
    allergics:Optional[List[str]]  #optional
    contact:Dict[str,str]

#function
def insert_patient_data(patient:Patient):
    print("Patient inserted successfully")
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedln_url)
    print(patient.married)
    print(patient.allergics)
    print(patient.contact)


#raw data
# Valid email + valid URL
patient_info1={
  "name": "Ankita Sharma",
  "email": "ankita@gmail.com",
  "linkedln_url": "https://www.linkedin.com/in/ankitasharma",
  "age": 28,
  "married": False,
  "allergics": ["dust", "pollen"],
  "contact": {
    "phone": "9876543210",
    "city": "Delhi"
  }
}

# #Invalid email + valid URL
# patient_info2={
#   "name": "Ravi Kumar",
#   "email": "ravi#gmail.com", #Invalid email
#   "linkedln_url": "https://www.linkedin.com/in/ravikumar",
#   "age": 32,
#   "allergics": ["milk"],
#   "contact": {
#     "phone": "9123456780",
#     "city": "Mumbai"
#   }
# }

# #Invalid email + invalid URL
# patient_info3={
#   "name": "Sneha Reddy",
#   "email": "sneha.com", #Invalid email
#   "linkedln_url": "linkedin-profile", #invalid URL
#   "age": 24,
#   "allergics": ["milk"],
#   "contact": {
#     "phone": "9012345678",
#     "city": "Hyderabad"
#   }
# }

#make pydantic object 1 for first patient
patient1=Patient(**patient_info1)

# #make pydantic object 2 for second patient
# patient2=Patient(**patient_info2)

# #make pydantic object 3 for third patient
# patient3=Patient(**patient_info3)

#pass object1 to function
insert_patient_data(patient1)

# #pass object2 to function
# insert_patient_data(patient2)

# #pass object3 to function
# insert_patient_data(patient3)
