from pydantic import BaseModel

class Pets(BaseModel):
    name: str
    race: str
    birthdate: str
    age: int
    description: str
    gender: str
    location: str