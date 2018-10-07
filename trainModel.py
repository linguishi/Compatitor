# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import json
from preProcess import simpleTokenize
from data.data_utils import getStopWords
from gensim import corpora, models, similarities


def generateModel(fileName='RawData20160307.json'):
    RawData = open(fileName, 'r')
    stopWords = getStopWords()
    print "prepocessing the RawData...",
    texts = [simpleTokenize(json.loads(
        line)['AppName']+' '+json.loads(line)['Description'], stopWords) 
        for line in RawData]
    RawData.close()    
    print "prepocessing the RawData Done!"

    print "generating a dictionary...",
    dictionary = corpora.Dictionary(texts)
    once_ids = [tokenid for tokenid,
                docfreq in dictionary.dfs.iteritems() if docfreq == 1]
    dictionary.filter_tokens(once_ids)
    dictionary.compactify()
    print "generating a dictionary Done!"
    # create a dir called modelfile
    print dictionary
    datapath = os.path.join(os.getcwd(), 'data')
    if not os.path.isdir(datapath):
        os.mkdir(datapath)
    dicFilePath = os.path.join(datapath, 'appdesc.dict')
    if os.path.isfile(dicFilePath):
        os.remove(dicFilePath)
    dictionary.save(dicFilePath)

    print "generating a Coupus...",
    corpus = [dictionary.doc2bow(text) for text in texts]
    mmFlePath = os.path.join(datapath, 'appdesc.mm')
    if os.path.isfile(mmFlePath):
        os.remove(mmFlePath)
    corpora.MmCorpus.serialize(mmFlePath, corpus, progress_cnt=10000)
    print "Done!"

    # Creating a transformation,train the TF-IDF model
    print "training the tfidf model...",
    tfidf = models.TfidfModel(corpus)  # step 1 -- initialize a model
    tfidfFilePath = os.path.join(datapath, 'model.tfidf_model')
    if os.path.isfile(tfidfFilePath):
        os.remove(tfidfFilePath)
    tfidf.save(tfidfFilePath)
    corpus_tfidf = tfidf[corpus]
    print "Done!"

    print "Mapping from tfidf to lsi...",
    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=300)
    corpus_lsi = lsi[corpus_tfidf]
    lsiFilePath = os.path.join(datapath, 'model.lsi')
    if os.path.isfile(lsiFilePath):
        os.remove(lsiFilePath)
    lsi.save(lsiFilePath)
    print "Done!"

    # transform corpus to LSI space and index it
    print "Generating the index...",
    index = similarities.MatrixSimilarity(corpus_lsi)
    indexFilePath = os.path.join(datapath, 'appdesc.index')
    if os.path.isfile(indexFilePath):
        os.remove(indexFilePath)
    index.save(indexFilePath)
    print "done!"


if __name__ == "__main__":
    generateModel('data/filterByLang.json')
