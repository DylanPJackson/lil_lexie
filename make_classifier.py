import pickle
import nltk
from nltk import DefaultTagger, UnigramTagger, BigramTagger, TrigramTagger
import nltk.tag.sequential

train_sents = nltk.corpus.brown.tagged_sents()
train_sents += nltk.corpus.conll2000.tagged_sents()
train_sents += nltk.corpus.treebank.tagged_sents()
t0 = DefaultTagger('NN')
t1 = UnigramTagger(train_sents, backoff=t0)
t2 = BigramTagger(train_sents, backoff=t1)
trigram_tagger = TrigramTagger(train_sents, backoff=t2) 
save_classifier = open("naivebayes.pickle", "wb")
pickle.dump(trigram_tagger, save_classifier)
save_classifier.close()    
