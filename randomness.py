import string
import random

def matched_brackets(str):
    count = 0
    for i in str:
        if i == "[":
            count += 1
        elif i == "]":
            count -= 1
        if count < 0:
            return False
    return count == 0

def generate_rule(N=5, alphabet='FXY', symbols='[]+-'):
    while True:
        random_rule = ''.join(random.choice(alphabet + symbols) for _ in range(N))
        if matched_brackets(random_rule):
            break
    return random_rule

def generate_axiom(alphabet='FXY'):
    return random.choice(alphabet)