from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Item(BaseModel):
    id: int
    name: ModelName
    
app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        model = Item(id=1, name=model_name)
        return model

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

print(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))