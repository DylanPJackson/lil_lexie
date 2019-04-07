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
    sentence = "sink"

api = datamuse.Datamuse()

def countLines(file):
    with open(file) as f:
        lines = f.read().splitlines()
    return lines



pronounList = countLines("C:/Users/Chubop/PycharmProjects/lil_lexie/pronouns")
nounList = countLines("C:/Users/Chubop/PycharmProjects/lil_lexie/nouns")
verbPhraseList = countLines("C:/Users/Chubop/PycharmProjects/lil_lexie/verb phrases")
verbList = countLines("C:/Users/Chubop/PycharmProjects/lil_lexie/verbs")

api = datamuse.Datamuse()

def makeRhyme(o):

    foo_complete = api.words(rel_rhy=o, max=25)
    list = []
    for x in foo_complete:
        list.append(x.get("word"))
    print(list)
    return list

def makeAntonym(o):
    foo_complete = api.words(rel_ant=o, max=25)
    list = []
    for x in foo_complete:
        list.append(x.get("word"))
    print(list)
    return list



def makeSentenceWithNoun(cfg):
    word = cfg.sentence
    if(cfg.isNoun == True):

        verbPhrase = verbPhraseList[randint(1, len(verbPhraseList)) - 1]
        pronoun = pronounList[randint(1, len(pronounList)) - 1]
        cfg.sentence = "I'll " + verbPhrase + " " + pronoun + " " + word

    return cfg.sentence

def makeSentenceWithVerb(cfg):
    pass

def makeCouplet(word):
    sentence = word
    verbPhrase = verbPhraseList[randint(1, len(verbPhraseList)) - 1]
    pronoun = pronounList[randint(1, len(pronounList)) - 1]
    noun = nounList[randint(1, len(nounList)) - 1]

    verb = verbList[randint(1, len(verbList)) - 1]
    couplet = verb + " " + pronoun + " " + noun + " " +  verbPhrase + " " + "a " + sentence
    return couplet

def findVerbRhyme(word):
    foo_complete = api.words(rel_rhy=word, max=25)
    list = []
    for x in foo_complete:
        list.append(x.get("word"))
    for x in list:
        for y in verbList:
            if x == y:
                return y

def makeCoupletVerb(word):
    verbPhrase = verbPhraseList[randint(1, len(verbPhraseList)) - 1]
    sentence = word
    list = makeAntonym(word)
    couplet = "You " + list[randint(0, len(list)-1)] + " I " + sentence
    return couplet

def checkNoun(word):
    for x in nounList:
        if(x == word):
            return True
    return False


def main():
    rhymes = makeRhyme("sink")
    cfg = CFG()
    print(makeSentenceWithNoun(cfg))
    word = rhymes[randint(0, len(rhymes)-1)]
    while(checkNoun(word) != True):
        word = rhymes[0]

    print(checkNoun(word))
    vRhyme = findVerbRhyme(word)
    print(makeCoupletVerb(vRhyme))
()

if __name__ == "__main__":
    main()