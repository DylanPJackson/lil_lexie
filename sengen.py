from random import randint

"""

File: sengen.py
Generate sentences using context-free grammars.

"""

import random as rand

class CFG:
    isNoun = True
    isVerb = False
    isAdj = False
    sentence = "fridge"


def countLines(file):
    with open(file) as f:
        lines = f.read().splitlines()
    return lines



def makeSentence(cfg):
    word = cfg.sentence
    if(cfg.isNoun == True):

        pList = countLines("C:/Users/Chubop/PycharmProjects/lil_lexie/pronouns")
        vpList = countLines("C:/Users/Chubop/PycharmProjects/lil_lexie/verb phrases")
        verbPhrase = vpList[randint(1, len(vpList))-1]
        pronoun = pList[randint(1, len(pList))- 1]
        cfg.sentence = verbPhrase + " " + pronoun + " " + word

    return cfg.sentence

def main():
    print("dog")
    cfg = CFG()
    print(makeSentence(cfg))


if __name__ == "__main__":
    main()