#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 16:52:05 2020

@author: claudiasatterfield
"""

        
class Catalog:
    def __init__(self):
        self._id = ""
        self._document_name = ""
        self._semester = ""
        self._year = ""
        
    def getId(self):
        return self._id
    
    def setId(self,id):
        self._id = id
        
    def getDocumentName(self):
        return self._document_name
    
    def setDocumentName(self, document_name):
        self._document_name = document_name
        
    def getSemester(self):
        return self._semester
    
    def setSemester(self, semester):
        self._semester = semester
        
    def getYear(self):
        return self._year
    
    def setYear(self, year):
        self._year = year  
    