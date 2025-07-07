import random
import time

subjects = ["You", "Your mind", "Your effort", "Success", "Happiness", "Discipline"]
verbs = ["is", "creates", "defines", "shapes", "drives", "builds"]
objects = ["your future", "your destiny", "the path to greatness", "everything", "who you become"]
endings = ["— keep going.", "— stay strong.", "— never stop.", "— believe in it.", "— own it."]

def generate_quote():
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    obj = random.choice(objects)
    ending = random.choice(endings)
    return f"{subject} {verb} {obj} {ending}"

print("✨ Random Inspirational Quote Generator ✨")
print("Press Ctrl+C to stop\n")

try:
    while True:
        print(generate_quote())
        time.sleep(2)
except KeyboardInterrupt:
    print("\nGoodbye! 💡")
