#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 11:56:42 2020

@author: claudiasatterfield
"""

import courses

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