from random import randint, choice

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(pass_length):
        password += choice(elements)
    return password
def kill(free):
    player = randint(1, free)
    bullet = randint(1, free)
    if player == bullet:
        return False
    return True 
