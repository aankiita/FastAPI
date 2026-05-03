from fastapi import FastAPI,Path,HTTPException,Query
from pydantic import BaseModel,computed_field,Field
from typing import Literal,Annotated
import json
from fastapi.responses import JSONResponse

app = FastAPI()

#define pydantic
class Patient(BaseModel):
    id:Annotated[str,Field(...,description="ID of the patient",example="P001")]
    name:Annotated[str,Field(...,description="Name of the patient")]
    city:Annotated[str,Field(...,description="",example="city where patient lives")]
    age:Annotated[int,Field(...,gt=0,lt=100,description="Age of the patient")]
    gender:Annotated[Literal['male','female'],Field(...,description="gender of patient")]
    height:Annotated[float,Field(...,description="",example="")] 
    weight:Annotated[float,Field(...,description="",example="")]

    @computed_field
    @property
    def bmi(self) -> float:  #float is output datatype of bmi.
        bmi=round(self.weight / (self.height ** 2), 2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:  #str is output datatype of verdict.
        if self.bmi<18.5 :
            return "underweight"
        elif self.bmi>=18.5 and self.bmi<30:
            return "normal"
        else:
            return "obese"

#get all the data from json file 
def load_data():
    with open('patient.json','r') as f:
        data=json.load(f)
    return data

#save data as dictionary(using dump) after making modification
def save_data(data):
    with open('patient.json','w') as f:
        json.dump(data,f) #This converts Python dictionary → JSON format and and writes it directly into a file

@app.get("/")
def hello():
    return {"message":"Patient Management System"}

@app.get("/view")
def view():
    data=load_data() #function call
    return data

@app.get('/view/patient/{patient_id}')
def view_patient(patient_id:str=Path(...,description='Id of patient in the DB',example='P001')):
    #load data-->function call
    data=load_data()

    #chcek if patient_id exist or not
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail='patient not found')

@app.get('/sort')
def sort_by_patients(sort_by:str=Query(...,description='sort on the basis of height,weight or bmi'),
                     order:str=Query('asc',description='sort in asc or desc order')):
    valid_field=['height','weight','bmi']

    if sort_by not in  valid_field:
        raise HTTPException(status_code=400,detail=f'Invalid,field select from {valid_field}')
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='Invalid, select order between asc or desc ')
    
    #load data
    data=load_data()

    #sort 
    sort_order=True if order=='desc' else False
    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)

    return sorted_data

#create route
@app.post("/create")
def create_patient(patient:Patient):
    #load data
    data=load_data()

    #check if patient already exist
    if patient.id in data:
        raise HTTPException(status_code=404,detail='patient already exist')
    
    #if new patient come -->model_dump() converts it into dictionary
    data[patient.id]=patient.model_dump(exclude=['id'])  #data[patient.id] means use patient.id as key
    #exclude=['id']-->Because id is already used as key

    #save into json file
    save_data(data)

    #send respose to user that we saved data
    return JSONResponse(status_code=201,content={'message':'patient created successfully'})
    
