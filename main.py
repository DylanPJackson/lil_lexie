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
stop = stopwords.words('english')
NOUNS = ['NN', 'NNS', 'NNP', 'NNPS']
VERBS = ['VB', 'VBG', 'VBD', 'VBN', 'VBP', 'VBZ']
ADJ = ['JJ']
POS = [NOUNS, VERBS, ADJ]

def get_objects(parsed, pos):
    # Get objeccts for given pos 
    objects = [p[0] for p in parsed if p[0] != 'i' and p[1] in POS[pos]]
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
    fdist = nltk.FreqDist(words) 
    # Determines most frequent nouns. pos_tag does not identify nouns
    # as well as tagger does. Therefore, these aren't REALLY the most
    # frequent nouns
    parsed = tagger.tag(words)
    #print("parsed: " + str(parsed))
    # Determine most probable object nouns
    #print("pos: " + str(pos))
    objects = get_objects(parsed, pos)
    return objects


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
        pos = random.randint(0,2) 
        objects = identify_objects(phrase, trigram_tagger, pos) 
        print("Objects: " + str(objects))

main()
