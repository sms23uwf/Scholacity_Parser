"""
    learningobjective_course.py
    -----------------------------

    The LearningObjective_course class represents a briege between a
    learningobjective record and a course record in the database.

"""

__author__ = "Steven M. Satterfield"


class LearningObjective_course:
    def __init__(self):
        self._id = ""
        self._courseId = ""
        self._learningObjectiveId = ""

    def getId(self):
        return self._id

    def setId(self, id):
        self._id = id

    def getCourseId(self):
        return self._courseId

    def setCourseId(self, courseId):
        self._courseId = courseId

    def getLearningObjectiveId(self):
        return self._learningObjectiveId

    def setLearningObjectiveId(self, learningObjectiveId):
        self._learningObjectiveId = learningObjectiveId
