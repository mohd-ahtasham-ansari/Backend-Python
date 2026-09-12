import json

from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.responses import JSONResponse
from  pydantic import BaseModel ,Field , computed_field
from typing import Annotated , Literal

app = FastAPI()

# reading the data from json file
def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data


# to save updated data
def save_data(data):
    with open("patients.json","w") as f:
        json.dump(data , f,indent=4)

# model for creating new data
class Patient(BaseModel):
    id: Annotated[str, Field(..., description="Enter Patient id here", examples=["P001"])]
    name: Annotated[str, Field(..., description="Enter patient name", examples=["John Doe"])]
    age: Annotated[int, Field(..., gt=0, lt=120, description="Enter patient age", examples=[25])]
    gender: Annotated[Literal['Male', 'Female', 'Other'], Field(..., description="Enter patient gender", examples=["Male"])]
    height: Annotated[float, Field(..., gt=0, description="Enter patient height", examples=[5.8])]
    weight: Annotated[float, Field(..., gt=0, description="Enter patient weight", examples=[70.0])]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = self.weight / (self.height * self.height)
        return round(bmi, 2)
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi >= 18.5 and self.bmi < 24.9:
            return "Normal"
        elif self.bmi >= 25 and self.bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"
        


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
def view_patient(patient_id: str = Path(..., description="Enter Patient id here", examples=["P001"])): # for show example in docs 
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

    
@app.post('/create')
def create_patient(patient:Patient):
    # load data from database
    data = load_data()

    #check if the patient aready exist
    if patient.id in data:
        raise HTTPException(status_code=400 , detail=f"patient with id {patient.id} already exist")

    #add pateint to data
    # our data is in pydantic model , we need to convert it into dict using json_dump
    data[patient.id] = patient.model_dump(exclude=['id'])

    # save data into json file
    save_data(data)

    return JSONResponse(status_code=201 , content={"message":"patient created sucessfully"})
