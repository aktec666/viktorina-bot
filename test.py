import random

def choice(*temp):
    print(temp)
    return random.choice(temp)

print(choice(1,6,4,79,23))