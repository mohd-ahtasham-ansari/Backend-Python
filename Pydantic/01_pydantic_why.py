from pydantic import BaseModel
from typing import List , Dict ,Optional


# def insert_pateint(name:str ,age:int):

#     if age <0:
#         raise ValueError("age cant be negative")
    
#     if age >110:
#         raise ValueError("age cant be greater than 110")

#     if type(name)== str and type(age)== int:
#         print(name)
#         print(age)
#         print("pateint data inserted")
#     else:
#         raise TypeError("invalid data type , please enter str and int")

# insert_pateint("ayush",23)

# def update_patient(name:str ,age :int):

#     if age <0:
#         raise ValueError("age cant be negative")
    
#     if age >110:
#         raise ValueError("age cant be greater than 110")

#     if type(name)== str and type(age)== int:
#         print(name)
#         print(age)
#         print("pateint updated successfully")
#     else:
#         raise TypeError("invalid data type , please enter str and int")

# """
# These are example of data validation , we cant handle every functions data validation , so it is not scaleable, that is why we use pydantic for data validation
# """

""" Data VALIDATION USING PYDANTIC """

class Patient(BaseModel):
    name:str
    age:int
    weight:float
    married:bool
    allergies: Optional[List[str]]=None
    contact_details: Dict[str,str]


def insert_pateint_info(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("pateint data inserted")

def update_patient_info(pateint:Patient):
    print(pateint.name)
    print(pateint.age)
    print(pateint.weight)
    print(pateint.married)
    print(pateint.allergies)
    print(pateint.contact_details)
    print("pateint updated successfully")


pateint_info = {"name":"ayush", "age":30,"weight":70.5,"married":True,"allergies":["peanuts","dust"],"contact_details":{"email":"[EMAIL_ADDRESS]","phone":"1234567890"}}

patient1= Patient(**pateint_info)

insert_pateint_info(patient1)

update_patient_info(patient1)

# """ lemme create an example of student info , data validation using pydantic  """

# class Student(BaseModel):
#     name:str
#     class_std:int
#     age:int
#     roll_no:int
#     student_id:str

# def insert_student_info(student:Student):
#     print(f"name - {student.name}")
#     print(f"class - {student.class_std}")
#     print(f"age - {student.age}")
#     print(f"roll no - {student.roll_no}")
#     print(f"student id - {student.student_id}")
#     print("Student data inserted")

# def update_student_info(student:Student):
#     print(f"name - {student.name}")
#     print(f"class - {student.class_std}")
#     print(f"age - {student.age}")
#     print(f"roll no - {student.roll_no}")
#     print(f"student id - {student.student_id}")
#     print("Student data updated")

# student_info={"name":"steve","class_std":12 , "age": 19,"roll_no":1, "student_id":"20120"}

# student1=Student(**student_info)


# insert_student_info(student1)
