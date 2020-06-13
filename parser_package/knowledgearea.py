"""
    knowledgearea.py
    ------------------

    The KnowledgeArea class represents a KnowledgeArea record in the database.

"""

__author__ = "Steven M. Satterfield"


class KnowledgeArea:
    def __init__(self):
        self._id = ""
        self._text = ""

    def getId(self):
        return self._id

    def setId(self, id):
        self._id = id

    def getText(self):
        return self._text

    def setText(self, text):
        self._text = text
