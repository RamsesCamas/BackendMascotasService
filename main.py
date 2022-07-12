from fastapi import FastAPI
from routes.pets import pet_router

app = FastAPI()

app.include_router(pet_router)