from fastapi import FastAPI
import random

app = FastAPI()

@app.post("/reset")
def reset():
    return {"state": 0}

@app.post("/step")
def step(action: int = 0):
    reward = random.randint(0, 1)
    done = random.choice([True, False])
    return {"state": random.randint(0, 10), "reward": reward, "done": done}
