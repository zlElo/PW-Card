import random
import string

def id_gen():
    characters = string.ascii_letters + string.digits
    id = 'ID-'
    
    for i in range(10):
        item = random.choice(characters)
        id += f'{item}'

    return id
