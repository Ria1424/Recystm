!pip install pymongo
import pymongo
from pymongo import MongoClient
import pandas as pd
import json

client = pymongo.MongoClient("mongodb://localhost:27017/")

df=pd.read_csv('/content/ds1.csv', encoding='latin-1', sep=';', on_bad_lines='skip')

df.head()

df.tail()

df.shape

data = df.to_dict(orient = "records")
data

db = client["RecSys"]
db
db.ds1.insert_many(data)
#done
