"""
    catalog.py
    --------------

    The Catalog class represents a Catalog record in the database.

"""

__author__ = "Steven M. Satterfield"

        
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
    