from pydantic import BaseModel,computed_field

from fastapi import FastAPI
app = FastAPI()

#Nested Address pydantic model
class Address(BaseModel):
    street: str
    city: str
    state: str
    pincode: str

# Main Patient pydantic model
class Patient(BaseModel):
    name: str
    age: int
    gender:str
    address: Address 

#function
def insert_patient_data(patient:Patient):
    print("Patient inserted successfully")
    print(patient.name)
    print(patient.age)
    print(patient.gender)
    print("\n")
    print(patient.address.pincode)
    print(patient.address.city)
    print(patient.address.state)
    print(patient.address.street)
    print("\n")

#raw data
patient_info1={
  "name": "Ankita Sharma",
  "age": 28,
  "gender": "female",
  "address": {
    "street": "MG Road",
    "city": "Delhi",
    "state": "Delhi",
    "pincode": "110001"
  }
}

patient_info2={
  "name": "Ravi Kumar",
  "age": 35,
  "gender": "male",
  "address": {
    "street": "Brigade Road",
    "city": "Bangalore",
    "state": "Karnataka",
    "pincode": "560001"
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
