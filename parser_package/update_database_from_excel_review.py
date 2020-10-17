"""
    update_database_from_excel_review.py
    --------------------------------------

    This module contains a set of functions that read the reviewed learning
    objectives from the excel file and update the database. If a new learning
    objective has been added to the excel file, it will be added against the
    appropriate course. If a learning objective has been designated as REMOVE
    then it will be removed from the database.

"""

__author__ = "Steven M. Satterfield"

import xlrd
from firebase import firebase
import datetime
import time

from catalog import Catalog
from knowledgearea import KnowledgeArea
from learningobjective_course import LearningObjective_course

firebase = firebase.FirebaseApplication('https://scholacity-org.firebaseio.com/')

catalogs = []
knowledgeAreas = []
lo_courses = []
catalogId = ""

workbook = xlrd.open_workbook('../inputs/Course_Catalog_Reviewed.xlsx')


def GetCatalogRecords(firebase: firebase) -> None:
    """
        Get existing catalog records from database and insert into global collection.

        :param firebase: a firebase connection

    """

    global catalogs
    global catalogId

    obj_key_list = []

    result = firebase.get('/catalog', None)

    if result is None:
        return

    for i in result.keys():
        obj_key_list.append(i)
        catalogId = i
        

    for i in obj_key_list:
        catalog = Catalog()
        catalog.setId(i)
        catalog.setDocumentName(result[i]['document_name'])
        catalog.setSemester(result[i]['semester'])
        catalog.setYear(result[i]['year'])
        catalogs.append(catalog)


def GetKnowledgeAreas(firebase: firebase) -> None:
    """
        Get  KnowledgeAreas from the database and
        insert them into the global collection.

        :param firebase: a firebase connection

    """

    global knowledgeAreas

    obj_key_list = []

    result = firebase.get('/knowledgearea', None)

    if result is None:
        return

    for i in result.keys():
        obj_key_list.append(i)

    for i in obj_key_list:
        knowledgeArea = KnowledgeArea()
        knowledgeArea.setText(result[i]['content'])
        knowledgeArea.setId(i)
        knowledgeAreas.append(knowledgeArea)


def GetBridgeRecords(firebase: firebase) -> None:
    """

        Get the learningobjective_course recordas and
        insert them into the global collection.

        :param firebase: a firebase connection

    """

    global lo_courses

    obj_key_list = []

    result = firebase.get('/learningobjective_course', None)

    if result is None:
        return

    for i in result.keys():
        obj_key_list.append(i)

    for i in obj_key_list:
        learningobjective_course = LearningObjective_course()
        learningobjective_course.setId(i)
        learningobjective_course.setLearningObjectiveId(result[i]['learningobjectiveid'])
        learningobjective_course.setCourseId(result[i]['courseid'])
        lo_courses.append(learningobjective_course)



def ApplyCourseTitleModificationToDatabase(firebase: firebase, courseId: str, titleModification: str) -> None:
    """

        This method will receive the courseId and the intended modifications and apply the changes to the database.

        :param firebase: a firebase connection
        :param courseId: str
        :param titleModification: str

    """

    print("courseId: {}, titleModification: {}".format(courseId, titleModification))

    if titleModification.strip() != "":
        updateLocation = "course" + "/" + courseId
        firebase.put(updateLocation, 'name', titleModification)


def ApplyCourseInstructorModificationToDatabase(firebase: firebase, courseId: str, instructorModification: str) -> None:
    """
    

        This method will receive the courseId and the intended modifications and apply the changes to the database.
        
        :param firebase: a firebase connection
        :param courseId: str
        :param instructorModification: str
        
    """
    
    print("courseId: {}, instructorModification: {}".format(courseId, instructorModification))

    if instructorModification.strip() != "":
        updateLocation = "course" + "/" + courseId
        firebase.put(updateLocation, 'instructor', instructorModification)
    
    
def ApplyCourseFeeModificationToDatabase(firebase: firebase, courseId: str, feeModification: float) -> None:
    """
    

        This method will receive the courseId and the intended modifications and apply the changes to the database.
        
        :param firebase: a firebase connection
        :param courseId: str
        :param feeModification: int
        
    """
    
    print("courseId: {}, feeModification: {}".format(courseId, feeModification))

    updateLocation = "course" + "/" + courseId
    firebase.put(updateLocation, 'fee', feeModification)
    
    
def ApplyCourseDescriptionModificationToDatabase(firebase: firebase, courseId: str, descriptionModification: str) -> None:
    """

        This method will receive the courseId and the intended modifications and apply the changes to the database.

        :param firebase: a firebase connection
        :param courseId: str
        :param descriptionModification: str

    """

    print("courseId: {}, descriptionModification: {}".format(courseId, descriptionModification))

    if descriptionModification.strip() != "":
        updateLocation = "course" + "/" + courseId
        firebase.put(updateLocation, 'description', descriptionModification)


def findKeyOfBridgeTableRecord(loId: str) -> str:
    """
    
        find and return the key value for a bridge table
        record for the provided learningobjectiveid
        
        :param loId: str
        
    """
    
    global lo_courses
    
    for bridgeRecord in lo_courses:
        bridgeId = bridgeRecord.getId()
        bridgeLoId = bridgeRecord.getLearningObjectiveId()
        
        if(bridgeLoId == loId):
            return bridgeId
        
    return ""


def ApplyLOModificationToDatabase(firebase: firebase, knowledgeAreaId: str, courseId: str, loId: str, modification: str) -> None:
    """

        This method will receive the courseId, the learningObjectiveId,
        and the intended modification and apply the change to the database.

        :param firebase: a firebase connection
        :param courseId: str
        :param loId: str
        :param modification: str

    """

    if loId.strip() == "-" or loId.strip() == "":

        newLearningObjective = {
            'courseid': courseId,
            'knowledgeareaid': knowledgeAreaId,
            'content': modification
        }
        result = firebase.post('learningobjective', newLearningObjective)
        newLoId = result.get("name")
        
        newBridgeRecord = {
            'courseid': courseId,
            'learningobjectiveid': newLoId
        }
        
        firebase.post('learningobjective_course', newBridgeRecord)
        
        print("just added learningobjective: {}".format(modification))

    else:

        if modification.strip().lower() == "remove":
            firebase.delete('learningobjective', loId)
            bridgeKey = findKeyOfBridgeTableRecord(loId)
            
            print("bridgeKey: {}".format(bridgeKey))
            if bridgeKey.strip().__len__() > 0:
                firebase.delete('learningobjective_course', bridgeKey)
                

        else:
            updateLocation = "learningobjective" + "/" + loId
            firebase.put(updateLocation, 'content', modification)
            print("just updated learningobjective: {}".format(modification))


def FindKnowledgeAreaId(KnowledgeAreaText: str) -> str:
    """
        Find existing KnowledgeArea in the global collection.
        If found, get the Id.

        :param newKnowledgeArea: a KnowledgeArea object

        :return string representation of the Id

    """

    global knowledgeAreas

    for KnowledgeArea in knowledgeAreas:
        if KnowledgeArea.getText().strip().lower() == KnowledgeAreaText.strip().lower():
            return KnowledgeArea.getId()

    return ""


def AddNewCourse(firebase: firebase, knowledgeArea: str, titleModification: str, descriptionModification: str, instructor: str, fee: float) -> None:
    """
        This method will add a new course under the knowledgeArea.
        
        :param firebase: a firebase connection
        :param knowledgeArea: str
        :param titleModification: str
        :param descriptionModification: str
 
    """

    global catalogId
    
    knowledgeAreaId = FindKnowledgeAreaId(knowledgeArea)
    
    newCourse = {
        'catalogid': catalogId,
        'knowledgeareaid': knowledgeAreaId,
        'name': titleModification,
        'description': descriptionModification,
        'instructor': instructor,
        'fee': fee
    }
    result = firebase.post('course', newCourse)
    

def AddNewSession(firebase: firebase, courseId: str, session_number: int, DOW: str, session_date: datetime, session_time_start: str, session_time_end: str) -> None:
    """
        This method will add a new session.
        
        :param firebase: a firebase connection
        :param courseId: str
        :param session_number: int
        :param DOW: str
        :param session_date: datetime
        :param session_time_start: str
        :param session_time_end: str
        
 
    """

    global catalogId
    
   
    newSession = {
        'courseid': courseId,
        'session_number': session_number,
        'DOW': DOW,
        'session_date': session_date,
        'session_time_start': session_time_start,
        'session_time_end': session_time_end
    }
    result = firebase.post('session', newSession)



def AddNewCourseDOW(firebase: firebase, DOW: str, courseId: str) -> None:
    """
    

        This method will add a new course under the knowledgeArea.
        
        :param firebase: a firebase connection
        :param DOW: str
        :param courseId: str

    """
    
    newCourseDOW = {
        'DOW': DOW,
        'courseid': courseId
    }
    result = firebase.post('courses_dow', newCourseDOW)
    
    
    
def ProcessSessionsWorksheet(firebase: firebase) -> None:
    """

        This method will iterate through the rows in the Sessions worksheet
        and call a method to make any indicated modifications to the database.

        :param firebase: a firebase connection

    """

    global workbook

    column_knowlegeArea = 0
    column_courseId = 1
    column_session_number = 3
    column_DOW = 4
    column_date = 5
    column_time_start = 6
    column_time_end = 7
    
    ws = workbook.sheet_by_index(1)
    
    for row_idx in range(1, ws.nrows):
        knowledgeAreaText = str(ws.cell(row_idx, column_knowlegeArea).value)
        courseId = str(ws.cell(row_idx, column_courseId).value)
        session_number = int(ws.cell(row_idx, column_session_number).value)
        DOW = str(ws.cell(row_idx, column_DOW).value)
        session_date = xlrd.xldate_as_datetime((ws.cell(row_idx, column_date).value), workbook.datemode)
        session_time_start = xlrd.xldate_as_datetime((ws.cell(row_idx, column_time_start).value), workbook.datemode)
        session_time_end = xlrd.xldate_as_datetime((ws.cell(row_idx, column_time_end).value), workbook.datemode)
    
        AddNewSession(firebase, courseId, session_number, DOW, session_date, session_time_start, session_time_end)
    
    
    
    
def ProcessCoursesDOWWorksheet(firebase: firebase) -> None:
    """

        This method will iterate through the rows in the Courses_DOW worksheet
        and call a method to make any indicated modifications to the database.

        :param firebase: a firebase connection

    """

    global workbook

    column_DOW = 0
    column_courseId = 1
    
    ws = workbook.sheet_by_index(2)
    
    for row_idx in range(1, ws.nrows):
        DOW = str(ws.cell(row_idx, column_DOW).value)
        courseId = str(ws.cell(row_idx, column_courseId).value)
    
        AddNewCourseDOW(firebase, DOW, courseId)
    
    

def ProcessCoursesWorksheet(firebase: firebase) -> None:
    """

        This method will iterate through the rows in the Courses worksheet
        and call a method to make any indicated modifications to the database.

        :param firebase: a firebase connection

    """

    global workbook

    column_knowlegeArea = 0
    column_courseId = 1
    column_TitleModification = 3
    column_DescriptionModification = 5
    column_Instructor = 6
    column_Fee = 7

    ws = workbook.sheet_by_index(0)

    for row_idx in range(1, ws.nrows):
        knowledgeAreaText = str(ws.cell(row_idx, column_knowlegeArea).value)
        courseId = str(ws.cell(row_idx, column_courseId).value)
        titleModification = str(ws.cell(row_idx, column_TitleModification).value)
        descriptionModification = str(ws.cell(row_idx, column_DescriptionModification).value)
        instructor = str(ws.cell(row_idx, column_Instructor).value)
        fee = float(ws.cell(row_idx, column_Fee).value)

        if courseId.strip() != "":
            if titleModification.strip() != "":
                ApplyCourseTitleModificationToDatabase(firebase, courseId, titleModification)
    
            if descriptionModification.strip() != "":
                ApplyCourseDescriptionModificationToDatabase(firebase, courseId, descriptionModification)
                
            ApplyCourseInstructorModificationToDatabase(firebase, courseId, instructor)
            ApplyCourseFeeModificationToDatabase(firebase, courseId, fee)

        else:
            print("ADDING NEW COURSE")
            AddNewCourse(firebase, knowledgeAreaText, titleModification, descriptionModification, instructor, fee)
            
            
            
def IterateKnowledgeAreaSheets(firebase: firebase) -> None:
    """

        This method will iterate through all of the worksheets in the workbook
        and call a method to make any indicated modifications to the databae.

        :param firebase: a firebase connection

    """

    global workbook
    global knowledgeAreas

    column_courseId = 0
    column_loId = 2
    column_modification = 4

    for knowledgeArea in knowledgeAreas:
        ws = workbook.sheet_by_name(knowledgeArea.getText()[0:31])
        knowledgeAreaId = knowledgeArea.getId()

        for row_idx in range(1, ws.nrows):
            courseId = str(ws.cell(row_idx, column_courseId).value)
            loId = str(ws.cell(row_idx, column_loId).value)
            modification = str(ws.cell(row_idx, column_modification).value)

            if modification.strip() != "":
                ApplyLOModificationToDatabase(firebase, knowledgeAreaId, courseId, loId, modification)


if __name__ == "__main__":
    GetCatalogRecords(firebase)
    GetKnowledgeAreas(firebase)
    GetBridgeRecords(firebase)
    #ProcessCoursesWorksheet(firebase)
    #ProcessSessionsWorksheet(firebase)
    ProcessCoursesDOWWorksheet(firebase)
    #IterateKnowledgeAreaSheets(firebase)
