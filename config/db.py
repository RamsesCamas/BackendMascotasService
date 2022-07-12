from sqlalchemy import create_engine, MetaData
import pymysql
from dotenv import load_dotenv
import os
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Date, Text
import sqlalchemy

load_dotenv()

user = os.getenv("USER_DB")
password = os.getenv("PASSWORD_DB")
host = os.getenv("HOST_DB")
port = os.getenv("PORT_DB")
name_db = os.getenv("NAME_DB")

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{name_db}', pool_recycle=3600)

meta = MetaData()
if not sqlalchemy.inspect(engine).has_table("pet"):
    metadata = MetaData(engine)
    Table('pet', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(150)),
    Column('race', String(150)),
    Column('birthdate', Date),
    Column('gender', String(1)),
    Column('age', Integer),
    Column('description', Text),
    Column('location',String(255)),
    Column('image_url', Text)
    )
    metadata.create_all()
conn = engine.connect()