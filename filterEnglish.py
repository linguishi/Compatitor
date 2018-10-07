# -*- coding: utf-8 -*-
"""
Created on Tue Dec 08 16:36:48 2015

@author: guishi_lin
"""
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException
import json
import os


def isEnglish(text):
    if detect(text)=='en':
        return True
    else:
        return False


def filterRawDataByLang(inputFile,outputFile):
    """
    filer the non english description in the corpus inputFile
    """
    print "start to filter the raw data by language..."
    inputJsonFile = open(inputFile,'r')
    if os.path.isfile(outputFile):
        os.remove(outputFile)
    outputJsonFile = open(outputFile,'ab')
    count = 0
    checkNum = 0
    totalLines = lineCounts(inputFile)
    for line in inputJsonFile:
        jsonobj = json.loads(line)
        checkNum = checkNum + 1
        if checkNum > 0 :
            try:
                if(isEnglish(jsonobj["Description"])):
                    json.dump(jsonobj,outputJsonFile)
                    count = count + 1
                    if(checkNum%1000==0):
                        print "Processing %d / %d items..." % (checkNum, totalLines)
                    outputJsonFile.write('\n')
            except LangDetectException as e:
                print e
                continue
    outputJsonFile.close()
    inputJsonFile.close()
    print "total: %d en items" % (count,)


def testfilterJsonFile(filename):
    jsonFile = open(filename,'r')
    count = 0 
    print "start to filter the data..."
    for line in jsonFile:
        jsonobj = json.loads(line)
        print "-----------------------***----------------------"
        print jsonobj["AppName"],
        print detect(jsonobj["Description"])
        print jsonobj["Description"]
        count = count + 1
        if(count==20):break
    jsonFile.close()


def lineCounts(filename):
    f = open(filename,'r')
    i = 0
    for line in f:
        i = i+1
    f.close()
    return i
    

def findStartPoint(fromline,filename,target):
    f = open(filename,'r')
    i = 0
    rs = -1
    for line in f:
        i = i+1
        if i>=fromline:
#            print line
            if target==json.loads(line)['Appid']:rs = i+1
            elif i>(fromline+100): break
        else: continue
    f.close()    
    return rs

if __name__ == "__main__":
    filterRawDataByLang('data/RawData.json','data/filterByLang.json')
    toNum = lineCounts('data/filterByLang.json')
    