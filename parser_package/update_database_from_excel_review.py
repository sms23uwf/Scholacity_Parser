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


firebase = firebase.FirebaseApplication('https://scholacity-org-test.firebaseio.com/')

knowledgeAreas = []

workbook = xlrd.open_workbook('../inputs/Course_Catalog_Reviewed.xlsx')


def GetKnowledgeAreas(firebase: firebase) -> None:
    """
        Get  KnowledgeAreas from the database and
        insert them into the global collection.

        :param firebase: a firebase connection

    """

    global knowledgeAreas

    obj_key_list = []

    result = firebase.get('/KnowledgeArea', None)

    if result is None:
        return

    for i in result.keys():
        obj_key_list.append(i)

    for i in obj_key_list:
        knowledgeArea = KnowledgeArea()
        knowledgeArea.setText(result[i]['Content'])
        knowledgeArea.setId(i)
        knowledgeAreas.append(knowledgeArea)


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
        updateLocation = "Course" + "/" + courseId
        firebase.put(updateLocation, 'Name', titleModification)


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
        updateLocation = "Course" + "/" + courseId
        firebase.put(updateLocation, 'Description', descriptionModification)


def ApplyLOModificationToDatabase(firebase: firebase, courseId: str, loId: str, modification: str) -> None:
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
            'CourseId': courseId,
            'Text': modification
        }
        firebase.post('LearningObjective', newLearningObjective)

    else:

        if modification.strip().lower() == "remove":
            firebase.delete('LearningObjective', loId)
        else:
            updateLocation = "LearningObjective" + "/" + loId
            firebase.put(updateLocation, 'Text', modification)


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

        for row_idx in range(1, ws.nrows):
            courseId = str(ws.cell(row_idx, column_courseId).value)
            loId = str(ws.cell(row_idx, column_loId).value)
            modification = str(ws.cell(row_idx, column_modification).value)

            if modification.strip() != "":
                ApplyLOModificationToDatabase(firebase, courseId, loId, modification)


if __name__ == "__main__":
    GetKnowledgeAreas(firebase)
    ProcessCoursesWorksheet(firebase)
    #IterateKnowledgeAreaSheets(firebase)
