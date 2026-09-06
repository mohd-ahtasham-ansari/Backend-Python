def insert_pateint(name:str ,age:int):

    if age <0:
        raise ValueError("age cant be negative")
    
    if age >110:
        raise ValueError("age cant be greater than 110")

    if type(name)== str and type(age)== int:
        print(name)
        print(age)
        print("pateint data inserted")
    else:
        raise TypeError("invalid data type , please enter str and int")

insert_pateint("ayush",23)

def update_patient(name:str ,age :int):

    if age <0:
        raise ValueError("age cant be negative")
    
    if age >110:
        raise ValueError("age cant be greater than 110")

    if type(name)== str and type(age)== int:
        print(name)
        print(age)
        print("pateint updated successfully")
    else:
        raise TypeError("invalid data type , please enter str and int")

"""
These are example of data validation , we cant handle every functions data validation , so it is not scaleable, that is why we use pydantic for data validation
"""