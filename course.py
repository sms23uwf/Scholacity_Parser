#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 10:22:25 2020

@author: claudiasatterfield
"""
        
class Course:
    def __init__(self):
        self._knowledgearea = ""
        self._title = ""
        self._tocEntry = ""
        self._description = ""
        
    def getKnowledgeArea(self):
        return self._knowledgearea
    
    def setKnowledgeArea(self,knowledgearea):
        self._knowledgearea = knowledgearea
        
    def getTitle(self):
        return self._title
    
    def setTitle(self, title):
        self._title = title

    def getTOCEntry(self):
        return self._tocEntry
    
    def setTOCEntry(self, tocEntry):
        self._tocEntry = tocEntry
        
    def getDescription(self):
        return self._description
    
    def setDescription(self, description):
        self._description = description
        
  
   