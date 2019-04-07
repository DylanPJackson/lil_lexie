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
import pickle

api = datamuse.Datamuse()
"""train_sents = nltk.corpus.brown.tagged_sents()
train_sents += nltk.corpus.conll2000.tagged_sents()
train_sents += nltk.corpus.treebank.tagged_sents()    
t0 = DefaultTagger('NN')
t1 = UnigramTagger(train_sents, backoff=t0)
t2 = BigramTagger(train_sents, backoff=t1)
trigram_tagger = TrigramTagger(train_sents, backoff=t2)"""
tagger_f = open("naivebayes.pickle", "rb")
trigram_tagger = pickle.load(tagger_f)
tagger_f.close()

stop = stopwords.words('english')
NOUNS = ['NN', 'NNS', 'NNP', 'NNPS']
VERBS = ['VB', 'VBG', 'VBD', 'VBN', 'VBP', 'VBZ']
POS = [NOUNS, VERBS]

def countLines(file):
    with open(file) as f:
        lines = f.read().splitlines()
    return lines

pronounList = countLines("pronouns")
verbPhraseList = countLines("verb phrases")
nounList = countLines("nouns")
verbList = countLines("verbs")

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
                return(verb + " " + pronoun + " " + subject[0] + " " + verbPhrase + " " + pos[0][0])
                #print(str(makeSentenceWithNoun(subject[0], 0)) + \
                    #makeSentenceWithNoun(pos[0][0], 1)) 
    elif subject[1] in VERBS:
        # I'll [verb_phrase] [pronoun] [rhymed_noun], rest 
        antonyms = api.words(rel_ant=subject[0], max=20)
        #print("antonyms: " + str(antonyms))
        if antonyms == []:
            return 1
        best_antonyms = antonyms[:3]
        shuffle(best_antonyms)
        done = 0
        for antonym in best_antonyms:
            a = antonym.get("word")
            v_pos = tagger.tag([a])
            #print("v_pos: " + str(v_pos))
            #if v_pos[0][1] in VERBS:
                #print("1")
            rhymes = api.words(rel_rhy=v_pos[0][0])
            top_rhymes = rhymes[:5]
            #print("rhymes: " + str(top_rhymes))
            for rhyme in top_rhymes:
                r = rhyme.get("word")
                n_pos = tagger.tag([r])
                if n_pos[0][1] in NOUNS:
                    #print("2")
                    verbPhrase = verbPhraseList[random.randint(1, len(verbPhraseList)) - 1]
                    pronoun = pronounList[random.randint(1, len(pronounList)) - 1]
                    return("I'll " + verbPhrase + " " + pronoun + " " + n_pos[0][0] \
                        + " You " + subject[0] + " I " + v_pos[0][0]) 
                    #done = 1
            #if(done):
            #    break
                    
    else:
        #print("subject: " + str(subject))
        pass

"""
    Main functionality idk
"""
def main():
    # Gather training data and train tagger, making TrigramTagger
    noLoop = 0
    while(1):
        phrase = input("Enter rap phrase: ")
        while(1):
            if(noLoop == 20):
                print("Max word range hit, stopping infinite loop")
                noLoop = 0
                break
            pos = random.randint(0,1) 
            objects = identify_objects(phrase, trigram_tagger, pos) 
            print("objects: " + str(objects))
            if objects == []:
                noLoop = noLoop + 1
                print("Couldn't find any POS for that one")
                continue
            subject = objects[0]
            response = makeCouplet(subject, trigram_tagger)
            if(response == 1):
                continue
            else:
                return response 

print(main())
