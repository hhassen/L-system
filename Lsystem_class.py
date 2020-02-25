import random

class Lsystem:
    def __init__(self, axiom='', ruleset={}):
        self.axiom = axiom
        self.ruleset = ruleset
        self.generation = 0

    def process(self, original_string):
        #  process a string with ruleset and return next gen string
        tranformed_string = ""
        for letter in original_string:
            try:
                tranformed_string = tranformed_string + ruleOutput(self.ruleset[letter])
            except KeyError:
                tranformed_string = tranformed_string + letter
        self.generation += 1
        return tranformed_string

    def processGen(self, gen=1):
        #  process strings until the given generation
        actualString = self.axiom
        for i in range(gen):
            actualString = self.process(actualString)
        return actualString

    def getGeneration(self):
        return self.generation

class rule:
    def __init__(self,replacement,proba=1):
        self.replacement = replacement
        self.proba = proba


def checkRules(rules=[]):
    sum = 0
    for r in rules:
        sum += r.proba
    return True if sum == 1 else False

def ruleOutput(rules=[]):
    if checkRules(rules):
        rand_num = random.uniform(0,1)
        sum = 0
        for r in rules:
            sum += r.proba
            if rand_num < sum:
                return r.replacement
    else:
        raise Exception('the sum of probabilities is expected to be 1')