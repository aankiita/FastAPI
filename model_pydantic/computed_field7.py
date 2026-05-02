from pydantic import BaseModel,computed_field

from fastapi import FastAPI
app = FastAPI()

#define pydantic
class Patient(BaseModel):
    name:str
    height: float 
    weight: float

    @computed_field
    @property
    def bmi(self) -> float:  #float is output datatype of bmi
        bmi=round(self.weight / (self.height ** 2), 2)
        return bmi

#function
def insert_patient_data(patient:Patient):
    print("Patient inserted successfully")
    print(patient.name)
    print(patient.weight)
    print(patient.height)
    print(patient.bmi)
    print("\n")

#raw data
patient_info1={
  "name": "Ankita Sharma",
  "weight":58.0,
  "height":1.676
}

patient_info2={
  "name": "Abhay Sharma",
   "weight":65.0,
  "height":1.8034
}
#make pydantic object 1 for first patient
patient1=Patient(**patient_info1)

#make pydantic object 2 for second patient
patient2=Patient(**patient_info2)

#pass object1 to function
insert_patient_data(patient1)

#pass object2 to function
insert_patient_data(patient2)
