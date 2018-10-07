# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:08:41 2015

@author: guishi_lin
"""

import re
import os
from stemming.porter2 import stem
from data.data_utils import getStopWords

def simpleTokenize(string, stopWords):
    split_regex = r'\W+'
    """
    parameters: string
    return a list contain tokens
    """
    return [stem(s.lower()) for s in re.split(split_regex, string) 
        if len(s) > 1 and s.lower() not in stopWords]

if __name__ == "__main__":
    print "test stemming ... "
    example_words = ["python","pythoner","pythoning","pythoned","pythonly"]
    for w in example_words:
        print(stem(w))
    print "test tokenize"
    stopWords = getStopWords()
    testStr = """
    "Boost up Memory, Clean and Optimize Disk - ALL in ONE - Supported 30 languages
    Powerful and more features integrated in single app. I'll introduce family and 
    friends to use - William Adams. Just 10$, your Mac will be brought to another 
    level - Unnamed. have sent feedback can make Doctor Cleaner Master better. 
    Please check - Alan Moore.Fast and Powerful CPU, RAM, Disk, File cleaner. Ranked 
    in the top Paid App in 20 countries.New featuring Boost up Memory, Optimize Disk,
    bring your Mac's performance up to speed with these fantastic new features!
    Doctor Cleaner Master performs a comprehensive sweep for junk files that are often 
    left over after apps are uninstalled. Doctor Cleaner Master automatically reclaims 
    system memory when you close a memory-intensive app. Increasing the productivity 
    of your Mac! Primaty features: [Boost up Memory] - Automatically optimizes 
    memory when apps close - Reclaim unused memory to make it available for use by other 
    apps - Optimize memory with one click - Graph monitor to track real-time memory 
    status [Optimize Disk] - Clean temporary file such as logs, caches files, 
    downloads, etc. - Empty current user's Trash Can - Remind users to clean their 
    disk when necessary [Find Duplicate Files] - Files compared via our advanced
    SHA-1 hash checksum algorithm - Super fast and accurate duplicate detection- 
    Locate duplicate images, audio, archives, entire folders and more- Automatic
     one-click duplicate selection [Find Unused & Old Files]- Add multiple folders 
     for scanning - More condition with Size & Date- Automatic one-click scan
     We've worked hard to make Doctor Cleaner Master as simple and efficient as 
     possible for you to use. We would love to hear your thoughts and we value your 
     feeback.  Please comment on the App Store or submit your ideas to email: 
     contact@giauhuynh.com. Help us localize Doctor Cleaner Master to your native 
     language.  Please send email with title Localize Doctor Cleaner Master 
     to email: contact@giauhuynh.com."
    """
    print simpleTokenize(testStr, stopWords)
