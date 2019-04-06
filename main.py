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
stop = stopwords.words('english')
NOUNS = ['NN', 'NNS', 'NNP', 'NNPS']

"""
    Given a phrase, return the object of the sentence
"""
def identify_objects(phrase, tagger):
    # Tokenizes all words in phrase
    words = nltk.tokenize.word_tokenize(phrase) 
    # Set all to lowercase, remove stopwords
    words = [word.lower() for word in words if word not in stop]
    # Determines frequency of each word
    fdist = nltk.FreqDist(words) 
    # Determines most frequent nouns. pos_tag does not identify nouns
    # as well as tagger does. Therefore, these aren't REALLY the most
    # frequent nouns
    most_freq_nouns = [w for w, c in fdist.most_common(10) if \
        nltk.pos_tag([w])[0][1] in NOUNS]
    #print("mfn: " + str(most_freq_nouns))
    # Give proper POS tag to most_freq_nouns
    parsed = tagger.tag(most_freq_nouns)  
    #print("Parsed: " + str(parsed))
    # Determine most probable object nouns
    object_nouns = [p[0] for p in parsed if p[0] != 'i' and  p[1] in NOUNS]
    return object_nouns


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
        objects = identify_objects(phrase, trigram_tagger) 
        print("Objects: " + str(objects))

main()
