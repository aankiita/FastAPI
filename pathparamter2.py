from fastapi import FastAPI
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
def view_patient(patient_id:str):
    #load data-->function call
    data=load_data()

    #chcek if patient_id exist or not
    if patient_id in data:
        return data[patient_id]
    return {'error':'patient not found'}
