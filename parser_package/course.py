"""
    course.py
    --------------

    The Course class represents a Course record in the database.

"""

__author__ = "Steven M. Satterfield"


class Course:
    def __init__(self):
        self._id = ""
        self._knowledgeAreaId = ""
        self._catalogId = ""
        self._knowledgearea = ""
        self._title = ""
        self._tocEntry = ""
        self._description = ""

    def getId(self):
        return self._id

    def setId(self, id):
        self._id = id

    def getKnowledgeAreaId(self):
        return self._knowledgeAreaId

    def setKnowledgeAreaId(self, knowledgeAreaId):
        self._knowledgeAreaId = knowledgeAreaId

    def getKnowledgeArea(self):
        return self._knowledgearea

    def setKnowledgeArea(self, knowledgearea):
        self._knowledgearea = knowledgearea

    def getCatalogId(self):
        return self._catalogId

    def setCatalogId(self, catalogId):
        self._catalogId = catalogId

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
