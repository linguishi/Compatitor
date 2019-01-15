import os
dirpath_ = os.path.split(os.path.realpath(__file__))[0]


def getStopWords():
    stopWordsFile = open(os.path.join(dirpath_, "stopwords.txt"), 'r')
    stopwords = set([words[0:-1] for words in stopWordsFile])
    stopWordsFile.close()
    return stopwords


def lineCounts(filename):
    f = open(os.path.join(dirpath_, filename), 'r')
    i = 0
    for line in f:
        i = i + 1
    f.close()
    return i
