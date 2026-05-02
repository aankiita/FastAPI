from fastapi import FastAPI,Path,HTTPException,Query

app=FastAPI()
import json

#get all the data from json file 
def load_data():
    with open('patient.json','r') as f:
        data=json.load(f)
    return data

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
