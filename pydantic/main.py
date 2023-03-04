from typing import List, Optional
from pydantic import BaseModel, validator

class Person(BaseModel):
    name: str
    age: int = 18
    email: Optional[str]
    hobbies: List[str] = []
    
    @validator('age')
    def validate_age(cls, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        return age
    
    @validator('email')
    def validate_email(cls, email):
        if email and '@' not in email:
            raise ValueError("Invalid email format")
        return email
    
    @validator('hobbies')
    def validate_hobbies(cls, hobbies):
        if len(hobbies) > 5:
            raise ValueError("Too many hobbies, maximum is 5")
        return hobbies

# Valid input data
person1 = Person(name="John", age=25, email="john@example.com", hobbies=["reading", "swimming"])
print(person1)
# Output: Person(name='John', age=25, email='john@example.com', hobbies=['reading', 'swimming'])

# Invalid input data
try:
    person2 = Person(name="Jane", age=-1, email="invalid email", hobbies=["reading", "swimming", "traveling", "dancing", "cooking", "playing guitar"])
    validated_person2 = person2.validate()
except ValueError as e:
    print('--------------\n'+str(e))
# Output: Age cannot be negative
