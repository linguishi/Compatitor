import os
dirpath_ = os.path.split(os.path.realpath(__file__))[0]

def getStopWords():
    stopWordsFile = open(os.path.join(dirpath_, "stopwords.txt"), 'r')
    stopwords = set([words[0:-1] for words in stopWordsFile])
    stopWordsFile.close()
    return stopwords