import random

class NumberGuessEnv:
    def __init__(self):
        self.number = None
        self.steps = 0
        self.level = None

    def reset(self):
        self.level = random.choice(["easy", "medium", "hard"])

        if self.level == "easy":
            self.number = random.randint(1, 5)
        elif self.level == "medium":
            self.number = random.randint(1, 10)
        else:
            self.number = random.randint(1, 20)

        self.steps = 0
        return {"level": self.level}

    def step(self, action):
        self.steps += 1

        if action == self.number:
            reward = max(1, 10 - self.steps)
            return {"observation": "correct", "reward": reward, "done": True}

        elif action < self.number:
            return {"observation": "too low", "reward": -1, "done": False}

        else:
            return {"observation": "too high", "reward": -1, "done": False}

    def state(self):
        return {"steps": self.steps, "level": self.level}