#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 16:45:50 2020

@author: claudiasatterfield
"""

import csv
import constant
import nltk
import docx2txt
from textblob import TextBlob


knowledgeAreas = []
knowledgeAreas.append('Arts and Literature')
knowledgeAreas.append('Business, Finance, and Technology')
knowledgeAreas.append('Culinary and Food')
knowledgeAreas.append('Culture, Travel and Tours')
knowledgeAreas.append('Gardening and Environment')
knowledgeAreas.append('History and Current Affairs')
knowledgeAreas.append('Science and Health')

coursesFile1 = "ArtsAndLiterature.csv"
coursesFile2 = "Business.csv"
coursesFile3 = "Culinary.csv"
coursesFile4 = "Culture.csv"
coursesFile5 = "Gardening.csv"
coursesFile6 = "History.csv"
coursesFile7 = "Science.csv"

currentKnowledgeArea = ""
writeFile = "sentences.csv"

document = docx2txt.process('Fall2019_LLFullCatalog.docx')

blob = TextBlob(document)          

print(blob.parse())

with open(writeFile, 'w') as output:
    writer = csv.writer(output)
    for sentence in blob.sentences:
        writer.writerow([sentence.words])

