from pydantic import BaseModel ,EmailStr ,AnyUrl ,Field, field_validator , model_validator , computed_field
from typing import List , Dict ,Optional,Annotated



class Pateint(BaseModel):
    name:str
    age:int
    email:EmailStr
    weight:float
    height:float
    married:bool
    allergies: Optional[List[str]]=None    
    contact_details: Dict[str,str] 

    @computed_field(return_type=float)
    @property
    def bmi(self):
        bmi = self.weight / (self.height * self.height)
        return round(bmi,2)


    @model_validator(mode='after')
    def validate_emergency_contact(self):
        if self.age > 60 and 'emergency' not in self.contact_details:
            raise ValueError('Emergency contact not provided for patient above 60')
        return self


def update_pateint(pateint:Pateint):
    print(f"pateint{pateint}")
    print(f"email {pateint.email}")
    print(f"name {pateint.name}")
    print(f"age {pateint.age}")
    print(f"weight {pateint.weight}")
    print(f"height {pateint.height}")
    print(f"bmi {pateint.bmi}")
    print(f"married {pateint.married}")
    print(f"allergies {pateint.allergies}")
    print(f"contact_details {pateint.contact_details}")


"""                               Test 1                      """

patient_info ={"name":"rohit", "age":59,"email":"abc@hdfc.com","weight":70,"height":1.74,"married":False,"contact_details":{"phone":"1234567890","address":"123 Main St"}}

pateint1 = Pateint(**patient_info)

update_pateint(pateint1)