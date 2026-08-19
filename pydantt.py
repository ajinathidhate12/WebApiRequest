from pydantic import BaseModel,Field

    
class student(BaseModel):
    def __init__(self, name: str, age: int=Field(gt = 23)):
        self.name = name
        self.age = age


std= student(name="ajinath", age=20)        
print(std.name)
