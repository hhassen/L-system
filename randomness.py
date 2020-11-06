import string
import random

def matched_brackets(str):
    """ Return True only if right brackets equals left brackets in number """
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
    """ Generate a random rule, with balanced brackets' number
    N: rule length
    alphabet: list of alphabet to be used
    symbols: list of symbols to be used
    """
    while True:
        random_rule = ''.join(random.choice(alphabet + symbols) for _ in range(N))
        if matched_brackets(random_rule):
            break
    return random_rule

def generate_axiom(alphabet='FXY'):
    """ Generate a random axiom, using a specific alphabet """
    return random.choice(alphabet)
