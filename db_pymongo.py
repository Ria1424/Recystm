!pip install pymongo pandas scikit-learn numpy

import pandas as pd
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['recommender_system']
collection = db['shein']

df = pd.read_csv('/content/shein.csv')

def upload_to_mongodb(df):
    # Convert DataFrame to dictionary format for MongoDB insertion
    data = df.to_dict(orient='records')
    # Insert into MongoDB collection
    collection.insert_many(data)
    print(f"Uploaded {len(data)} records to MongoDB.")

upload_to_mongodb(df)
