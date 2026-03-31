from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class Action(BaseModel):
    action: int = 0

# Allow both GET and POST
@app.api_route("/reset", methods=["GET", "POST"])
def reset():
    return {
        "observation": 0,
        "reward": 0,
        "done": False,
        "info": {}
    }

@app.api_route("/step", methods=["GET", "POST"])
def step(action: Action = None):
    return {
        "observation": random.randint(0, 10),
        "reward": random.randint(0, 1),
        "done": random.choice([True, False]),
        "info": {}
    }
