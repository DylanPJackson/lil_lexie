from random import randint
from datamuse import datamuse

"""

File: sengen.py
Generate sentences using context-free grammars.

"""

import random as rand

class CFG:
    isNoun = True
    isVerb = False
    isAdj = False
    sentence = "shirt"
    rhyme = "yogurt"

api = datamuse.Datamuse()


def countLines(file):
    foo_complete = api.suggest(s="cat", max=10)
    "print(foo_complete)"
    with open(file) as f:
        lines = f.read().splitlines()
    return lines



pronounList = countLines("C:/Users/Chubop/PycharmProjects/lil_lexie/pronouns")
nounList = countLines("C:/Users/Chubop/PycharmProjects/lil_lexie/nouns")
verbPhraseList = countLines("C:/Users/Chubop/PycharmProjects/lil_lexie/verb phrases")
verbList = countLines("C:/Users/Chubop/PycharmProjects/lil_lexie/verbs")

api = datamuse.Datamuse()


def makeSentence(cfg):
    word = cfg.sentence
    if(cfg.isNoun == True):

        verbPhrase = verbPhraseList[randint(1, len(verbPhraseList)) - 1]
        pronoun = pronounList[randint(1, len(pronounList)) - 1]
        cfg.sentence = "I'll " + verbPhrase + " " + pronoun + " " + word

    return cfg.sentence

def makeCouplet(word):
    sentence = word
    verbPhrase = verbPhraseList[randint(1, len(verbPhraseList)) - 1]
    pronoun = pronounList[randint(1, len(pronounList)) - 1]
    noun = nounList[randint(1, len(nounList)) - 1]

    verb = verbList[randint(1, len(verbList)) - 1]
    couplet = verb + " " + pronoun + " " + noun + " " +  verbPhrase + " " + sentence
    return couplet


def main():
    print("dog")
    cfg = CFG()
    print(makeSentence(cfg))
    print(makeCouplet("yogurt"))


if __name__ == "__main__":
    main()