from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Date, Text

from config.db import meta


pets = Table('pet', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(150)),
    Column('race', String(150)),
    Column('birthdate', Date),
    Column('age', Integer),
    Column('gender', String(1)),
    Column('description', Text),
    Column('location',String(255)),
    Column('image_url', Text)
    )