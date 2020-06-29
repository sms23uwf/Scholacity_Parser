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

from knowledgearea import KnowledgeArea
from learningobjective_course import LearningObjective_course

firebase = firebase.FirebaseApplication('https://scholacity-org.firebaseio.com/')


knowledgeAreas = []
lo_courses = []

workbook = xlrd.open_workbook('../inputs/Course_Catalog_Reviewed.xlsx')


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
        :param descriptionModification: str

    """

    print("courseId: {}, titleModification: {}".format(courseId, titleModification))

    if titleModification.strip() != "":
        updateLocation = "course" + "/" + courseId
        firebase.put(updateLocation, 'name', titleModification)


def ApplyCourseDescriptionModificationToDatabase(firebase: firebase, courseId: str, descriptionModification: str) -> None:
    """

        This method will receive the courseId and the intended modifications and apply the changes to the database.

        :param firebase: a firebase connection
        :param courseId: str
        :param titleModification: str
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


def ProcessCoursesWorksheet(firebase: firebase) -> None:
    """

        This method will iterate through the rows in the Courses worksheet
        and call a method to make any indicated modifications to the database.

        :param firebase: a firebase connection

    """

    global workbook

    column_courseId = 1
    column_TitleModification = 3
    column_DescriptionModification = 5

    ws = workbook.sheet_by_index(0)

    for row_idx in range(1, ws.nrows):
        courseId = str(ws.cell(row_idx, column_courseId).value)
        titleModification = str(ws.cell(row_idx, column_TitleModification).value)
        descriptionModification = str(ws.cell(row_idx, column_DescriptionModification).value)


        if titleModification.strip() != "":
            ApplyCourseTitleModificationToDatabase(firebase, courseId, titleModification)

        if descriptionModification.strip() != "":
            ApplyCourseDescriptionModificationToDatabase(firebase, courseId, descriptionModification)


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
    GetKnowledgeAreas(firebase)
    GetBridgeRecords(firebase)
    ProcessCoursesWorksheet(firebase)
    IterateKnowledgeAreaSheets(firebase)
