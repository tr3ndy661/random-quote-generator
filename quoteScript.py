import random

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
print("Press Enter to get a new quote, or type 'q' to quit.\n")

while True:
    user_input = input(">> ")
    if user_input.lower() == 'q':
        print("Goodbye! 💡")
        break
    print(generate_quote())