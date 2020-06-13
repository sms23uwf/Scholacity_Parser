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
        self._text = ""

    def getId(self):
        return self._id

    def setId(self, id):
        self._id = id

    def getCourseId(self):
        return self._courseId

    def setCourseId(self, courseId):
        self._courseId = courseId

    def getText(self):
        return self._text

    def setText(self, text):
        self._text = text
