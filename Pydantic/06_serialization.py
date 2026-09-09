from pydantic import BaseModel

class Address(BaseModel):
    city : str
    state : str
    pin : str

class Patient(BaseModel):
    
    name : str
    gender : str
    age : int
    address : Address







address_dict ={"city":"mumbai" ,"state":"maharashtra" ,"pin":"400001"}

address1 = Address(**address_dict)

patient_dict = {"name":"rohit" ,"gender":"male" ,"age":25,"address":address1}

pateint1 = Patient(**patient_dict)


print(pateint1)

temp = pateint1.model_dump()

print(temp)
print(type(temp))

temp1 = pateint1.model_dump_json(exclude={"address":["state"]})

print(temp1)
print(type(temp1))
