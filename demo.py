from environment import NumberGuessEnv
import random

env = NumberGuessEnv()
print(env.reset())

guesses = list(range(1, 21))
random.shuffle(guesses)

for guess in guesses:
    result = env.step(guess)
    print(f"Guess: {guess}, Result: {result}")
    
    if result["done"]:
        print("🎉 Correct guess found!")
        break

print("Final State:", env.state())