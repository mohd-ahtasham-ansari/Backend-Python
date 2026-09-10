import json

from fastapi import FastAPI, HTTPException, Path, Query

app = FastAPI()

# reading the data from json file
def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

class Patient(BaseModel):
    name : str
    age : int
    gender : str
    height : float
    weight : float
    bmi : float

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
def view_patient(patient_id: str = Path(..., description="Enter Patient id here",  example="P001") ,): # for show example in docs 
    #load all the patient
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404 , detail="patient not found")  
@app.get("/sort")
def sort_patient(sort_by: str = Query(..., description = "Sort on the basis of Height , Weight or Bmi"),order : str = Query("asc", description = "sort asc or desc order")):
   

    valid_fields =['height','weight','bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=404 , detail=f"Invalid field selected , select from {valid_fields}") 
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400 , detail="Invalid order select between 'asc' and 'desc'" )
    
    data = load_data()

    sort_order = True if order =="desc" else False   

    sorted_data = sorted(data.values(),key=lambda x: x.get(sort_by , 0),reverse=sort_order)
    
    return sorted_data

    

    
    