import random

def get_randomdigit_jaindesmondblack(length):
    random_number = ""
    for n in range(length):
        random_number  += str(random.randint(0,9))
    return random_number
    