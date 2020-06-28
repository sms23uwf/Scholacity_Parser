"""
    courses.py
    --------------

    The Courses class represents a collection of Course objects.

"""

__author__ = "Steven M. Satterfield"


class CourseIterator:
    def __init__(self, courses):
        self._courses = courses
        self._index = 0
        
    def __next__(self):
        if self._index < (len(self._courses)):
            result = (self._courses[self._index])
            self._index += 1
            return result
        else:
            raise StopIteration
            
class Courses:
    def __init__(self):
        self._members = list()
        
    def addCourse(self, course):
        self._members += course
        
    def __iter__(self):
        return CourseIterator(self)
    
    