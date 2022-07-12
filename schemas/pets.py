from pydantic import BaseModel

class Pets(BaseModel):
    name: str
    race: str
    birthdate: str
    description: str
    gender: str
    location: str
    image_url: str