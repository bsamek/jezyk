import collections

import nltk
from nltk.corpus import brown

def gen_sentences(corpus):
    fdist = nltk.FreqDist(corpus.words())

    sentence_weights = {}
    for sentence in corpus.sents():
        weight = 0
        for word in sentence:
            weight += 1.0/fdist[word]
        sentence_weight = weight / len(sentence)

        sentence_weights[" ".join(sentence)] = sentence_weight

    sorted_sents = collections.OrderedDict(sorted(
        sentence_weights.items(), key=lambda t: t[1]))

    for i in range(100):
        print sorted_sents.items()[i]


if __name__ == "__main__":
    gen_sentences(brown)
