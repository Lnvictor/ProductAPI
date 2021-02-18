import pymongo
from decouple import config
from mongoengine import connect

host = config("HOST")
db = config("DB")
user = config("USERNAME")
pwd = config("PASSWORD")

conn = connect(db=db, username=user, password=pwd, host=host)
