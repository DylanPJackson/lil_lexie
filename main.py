"""
    file:
        main.py

    description:
        Main module to for lil_lexie program
    
    authors:   
        Dylan P. Jackson
        Samuel O. Kirby
        Justin T. Krumlauf
        Alex J. Lamarche
"""
import nltk
from nltk.corpus import stopwords
from nltk import DefaultTagger, UnigramTagger, BigramTagger, TrigramTagger
import nltk.tag.sequential
import random
from random import shuffle
from datamuse import datamuse

api = datamuse.Datamuse()
stop = stopwords.words('english')
NOUNS = ['NN', 'NNS', 'NNP', 'NNPS']
VERBS = ['VB', 'VBG', 'VBD', 'VBN', 'VBP', 'VBZ']
ADJ = ['JJ']
POS = [NOUNS, VERBS, ADJ]

def countLines(file):
    with open(file) as f:
        lines = f.read().splitlines()
    return lines

pronounList = countLines("pronouns.txt")
verbPhraseList = countLines("verb_phrases.txt")
nounList = countLines("nouns.txt")
verbList = countLines("verbs.txt")

def get_objects(parsed, pos):
    # Get objeccts for given pos 
    objects = [p for p in parsed if p[0] != 'i' and p[1] in POS[pos]]
    return objects

"""
    Given a phrase, return the object of the sentence
"""
def identify_objects(phrase, tagger, pos):
    # Tokenizes all words in phrase
    words = nltk.tokenize.word_tokenize(phrase) 
    # Set all to lowercase, remove stopwords
    words = [word.lower() for word in words if word not in stop]
    # Determines frequency of each word
    #fdist = nltk.FreqDist(words) 
    # Determines most frequent nouns. pos_tag does not identify nouns
    # as well as tagger does. Therefore, these aren't REALLY the most
    # frequent nouns
    parsed = tagger.tag(words)
    #print("parsed: " + str(parsed))
    # Determine most probable object nouns
    #print("pos: " + str(pos))
    objects = get_objects(parsed, pos)
    return objects

def makeSentenceWithNoun(noun, indicator):
    verbPhrase = verbPhraseList[random.randint(1, len(verbPhraseList)) -1]
    pronoun = pronounList[random.randint(1, len(pronounList)) -1]
    if indicator:
         return "You'll " + verbPhrase + " " + pronoun + " " + noun 
    else:
        return "I'll " + verbPhrase + " " + pronoun + " " + noun

def makeCouplet(subject, tagger):
    if subject[1] in NOUNS:
        #print("subject[1] in NOUNS: " + str(subject[1]))
        subject_rhymes = api.words(rel_rhy=subject[0], max=20)
        shuffle(subject_rhymes)
        for rhyme in subject_rhymes:
            r = rhyme.get("word")
            pos = tagger.tag([r])
            #print("pos: " + str(pos))
            if pos[0][1] in NOUNS:
                verb = verbList[random.randint(1, len(verbList)) - 1]
                pronoun = pronounList[random.randint(1, len(pronounList)) -1]
                verbPhrase = verbPhraseList[random.randint(1, len(verbPhraseList)) -1]
                print(verb + " " + pronoun + " " + subject[0] + " " + verbPhrase + " " + pos[0][0])
                #print(str(makeSentenceWithNoun(subject[0], 0)) + \
                    #makeSentenceWithNoun(pos[0][0], 1)) 
                break

"""
    Main functionality idk
"""
def main():
    # Gather training data and train tagger, making TrigramTagger
    train_sents = nltk.corpus.brown.tagged_sents()
    train_sents += nltk.corpus.conll2000.tagged_sents()
    train_sents += nltk.corpus.treebank.tagged_sents()    
    t0 = DefaultTagger('NN')
    t1 = UnigramTagger(train_sents, backoff=t0)
    t2 = BigramTagger(train_sents, backoff=t1)
    trigram_tagger = TrigramTagger(train_sents, backoff=t2)
    while(1):
        phrase = input("Enter rap phrase: ")
        #pos = random.randint(0,2) 
        pos = 0
        objects = identify_objects(phrase, trigram_tagger, pos) 
        #print("Objects: " + str(objects))
        subject = objects[0]
        makeCouplet(subject, trigram_tagger) 

main()
