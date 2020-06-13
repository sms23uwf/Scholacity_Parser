#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 18:25:35 2020

@author: Steven M. Satterfield
"""
class Run:
    def __init__(self):
        self._font = ""
        self._bold = ""
        self._italic = ""
        
    def getFont(self):
        return self._font
    
    def setFont(self, font):
        self._font = font

    def getBold(self):
        return self._bold
    
    def setBold(self, bold):
        self._bold = bold

    def getItalic(self):
        return self._italic
    
    def setItalic(self, italic):
        self._italic = italic


class Paragraph:
    def __init__(self):
        self._number = 0
        self._style = ""
        self._styleType = ""
        self._styleId = ""
        self._format = ""
        self._header = ""
        self._text = ""
        self._runCount = 0
        self._runs = []
        
    def getNumber(self):
        return self._number
    
    def setNumber(self,number):
        self._number = number
        
    def getStyle(self):
        return self._style
    
    def setStyle(self, style):
        self._style = style

    def getStyleType(self):
        return self._styleType
    
    def setStyleType(self, styleType):
        self._styleType = styleType

    def getStyleId(self):
        return self._styleId
    
    def setStyleId(self, styleId):
        self._styleId = styleId

    def getFormat(self):
        return self._format
    
    def setFormat(self, format):
        self._format = format

    def getHeader(self):
        return self._header
    
    def setHeader(self, header):
        self._header = header
        
    def getText(self):
        return self._text
    
    def setText(self, text):
        self._text = text
        
    def getRunCount(self):
        return self._runCount
    
    def setRunCount(self, runCount):
        self._runCount = runCount
        
    def getRuns(self):
        return self._runs
    
    def setRuns(self, run):
        self._runs.append(run)
    