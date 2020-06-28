"""
    learningobjective.py
    ---------------------

    The LearningObjective class represents a LearningObjective
    record in the database.

"""

__author__ = "Steven M. Satterfield"


class LearningObjective:
    def __init__(self):
        self._id = ""
        self._courseId = ""
        self._course = ""
        self._knowledgeAreaId = ""
        self._knowledgearea = ""
        self._text = ""

    def getId(self):
        return self._id

    def setId(self, id):
        self._id = id

    def getCourseId(self):
        return self._courseId

    def setCourseId(self, courseId):
        self._courseId = courseId

    def getCourse(self):
        return self._course

    def setCourse(self, course):
        self._course = course

    def getKnowledgeAreaId(self):
        return self._knowledgeAreaId

    def setKnowledgeAreaId(self, knowledgeAreaId):
        self._knowledgeAreaId = knowledgeAreaId

    def getKnowledgeArea(self):
        return self._knowledgearea

    def setKnowledgeArea(self, knowledgearea):
        self._knowledgearea = knowledgearea

    def getText(self):
        return self._text

    def setText(self, text):
        self._text = text
