from fastapi import APIRouter
from models.pets import pets
from config.db import conn
from schemas.pets import Pets

pet_router = APIRouter()

@pet_router.get('/')
async def index():
    return {"message":"Pet Microservice"}

@pet_router.get('/get_all')
async def get_all_pets():
    return conn.execute(pets.select()).fetchall()

@pet_router.get('/get/{id}')
async def get_pet(id: int):
    return conn.execute(pets.select().where(pets.c.id==id)).first()

@pet_router.post('/create')
async def create_pet(pet: Pets):
    conn.execute(pets.insert().values(
        name = pet.name,
        race = pet.race,
        birthdate = pet.birthdate,
        age = pet.age,
        description = pet.description,
        gender = pet.gender,
        location = pet.location
    ))
    return {"message": "ok"}

@pet_router.put('/update/{id}')
async def update_pet(id:int, pet: Pets):
    conn.execute(pets.update().values(
        name = pet.name,
        race = pet.race,
        birthdate = pet.birthdate,
        age = pet.age,
        description = pet.description,
        gender = pet.gender,
        location = pet.location
    ).where(pets.c.id==id))
    return conn.execute(pets.select().where(pets.c.id==id)).first()

@pet_router.delete('/delete/{id}')
async def delete_pet(id:int):
    conn.execute(pets.delete().where(pets.c.id==id))
    return {"message":"ok"}