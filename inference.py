from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

# Request model for step
class Action(BaseModel):
    action: int = 0

@app.post("/reset")
def reset():
    return {
        "observation": 0,
        "reward": 0,
        "done": False,
        "info": {}
    }

@app.post("/step")
def step(action: Action):
    return {
        "observation": random.randint(0, 10),
        "reward": random.randint(0, 1),
        "done": random.choice([True, False]),
        "info": {}
    }
