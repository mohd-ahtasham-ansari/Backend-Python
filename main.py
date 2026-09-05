from fastapi import FastAPI
import json

app = FastAPI()

# reading the data from json file
def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data


@app.get("/")
def hello():
    return {"message":"hello world"}

@app.get("/about")
def about():
    return {"message":"campusX is an education platform where you can learn ai"}

@app.get("/view")
def view_patients():
    data = load_data()
    return data

#viewing a specific patient using patient id
@app.get('/patient/{patient_id}')
def view_patient(patient_id: str):
    #load all the patient
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    return {"message": "patient not found"}