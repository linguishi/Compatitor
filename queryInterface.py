# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 10:14:12 2015

@author: guishi_lin
"""
from gensim import corpora, models, similarities, matutils
from filterEnglish import isEnglish
from preProcess import simpleTokenize
from data.data_utils import getStopWords
import json
import os

dirpath = os.path.split(os.path.realpath(__file__))[0]
datapath = os.path.join(dirpath, 'data')

# load dictoinary
print "Loading the dictionary..."
dictionary = corpora.Dictionary.load(os.path.join(datapath, 'appdesc.dict'))
# load the corpus
print "Loading the corpus..."
corpus = corpora.MmCorpus(os.path.join(datapath, 'appdesc.mm'))
# load the trained model
print "Loading the LSIMappingModel"
lsi = models.LsiModel.load(os.path.join(datapath, 'model.lsi'))
# load the LSI vetors distrubution
print "Loading the Index..."
index = similarities.MatrixSimilarity.load(
    os.path.join(datapath, 'appdesc.index'))

print "Loading the TFIDFModel..."
tfidf = models.TfidfModel.load(os.path.join(datapath, 'model.tfidf_model'))

stopWords = getStopWords()

def getAppidFromIndex(idx, corpusRawFile='data/filterByLang.json'):
    f = open(os.path.join(dirpath, corpusRawFile), 'r')
    count = 0
    for line in f:
        count = count + 1
        if count <= idx:
            continue
        jsonobj = json.loads(line)
        # the next line should be modified
        f.close()
        return jsonobj["Appid"]

def getDetailFromAppids(appids, corpusFile='data/filterByLang.json'):
    appids = map(str, appids)
    f = open(os.path.join(dirpath, corpusFile), 'r')
    rs = []
    for line in f:
        jsonObj = json.loads(line)
        if str(jsonObj['Appid']) in appids:
            rs.append(jsonObj)
    return rs

def getDescriptionFromAppid(appid):
    description = getDetailFromAppids([appid])
    return unicode(description[0]['AppName']+' '+description[0]['Description'], 'utf8')


def getLSIVector(text):
    stopWords = getStopWords()
    queryTokens = simpleTokenize(text, stopWords)
    queryBOWVec = dictionary.doc2bow(queryTokens)
    return lsi[tfidf[queryBOWVec]]


def queryByDescription(text, topNum=100):
    """
    input the appid
    return a list of appids contained in coupus that similar with the input
    """
    appidListSimilarity = []
#    if not isEnglish(text): return -1
    queryLSIVec = getLSIVector(text)
    index.num_best = topNum
    sims = index[queryLSIVec]
#    sims = sorted(enumerate(sims), key = lambda item: -item[1])
#    print sims[0:topNum]
    for item in sims:
        appidListSimilarity.append((getAppidFromIndex(item[0]), item[1]))
#    rmove sims when not debug
    return appidListSimilarity


def queryByAppid(appid, topNum=100):
    """
    input the appid
    return a list of appids contained in coupus that similar with the input
    """
    detail = getDetailFromAppids([appid])
    if len(detail) == 0:
        raise IndexError('oh my god')
    return queryByDescription(detail[0]['Description'], topNum)


def isCompatitor(enermyAppid, myAppid, threthold = 0.2):
    """
    input two appid
    print out the similarity of the two and return true or not
    """
    enermyLSI = getLSIVector(getDescriptionFromAppid(enermyAppid))
    myLSI = getLSIVector(getDescriptionFromAppid(myAppid))
    similarity = matutils.cossim(enermyLSI, myLSI)
    if similarity > threthold:
        return True, similarity
    else:
        return False, similarity


if __name__ == "__main__":
    answer = queryByAppid("921458519",5)
    for app in getDetailFromAppids(map(lambda x:x[0], answer)):
        print app
        print '-'*70 + '\n'
