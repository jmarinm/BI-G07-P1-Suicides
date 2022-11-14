import json
from typing import Optional
from fastapi import FastAPI
from models.DataModelList import DataModelList
from models.DataModel import DataModel
from PredictionModel import Model
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000/",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
   return {"Hello": "World"}

@app.post("/predict")
def make_predictions(data: DataModelList):
    records = data.records
    df = pd.DataFrame.from_records([r.to_dict() for r in records])
    df = df.append({"text":"aaa"}, ignore_index = True)
    model = Model()
    result = model.make_predictions(df)
    result = result.tolist()
    result = [p for p in result]
    res = {"Predictions": result}
    return res

