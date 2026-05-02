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


#make pydantic object 
patient1=Patient(**patient_info1)

#pass object to function
insert_patient_data(patient1)



#serialization(convert pydantic model as python dictionaries or Json format for storing as file)
#convert pydantic model as python dictionaries
temp=patient1.model_dump()
print(temp)
print(type(temp))

#convert pydantic model as json file
temp2=patient1.model_dump_json()
print(temp2)
print(type(temp2))
