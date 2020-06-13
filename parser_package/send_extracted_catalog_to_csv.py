"""
    send_extracted_catalog_to_csv.py
    --------------------------------

    This module contains a set of functions that read the extracted
    catalog data from the database and export it to Excel format along
    with the row Ids so that the data can be refined and the database
    can be updated.

"""

__author__ = "Steven M. Satterfield"

import xlsxwriter
from firebase import firebase

from knowledgearea import KnowledgeArea
from learningobjective import LearningObjective
from course import Course


firebase = firebase.FirebaseApplication('https://scholacity-org-test.firebaseio.com/')

knowledgeAreas = []
courses = []
learningObjectives = []

workbook = xlsxwriter.Workbook('Course_Catalog_Review.xlsx')


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


def GetCourses(firebase: firebase) -> None:
    """

        Get Courses from the database and insert them into the
        global collection.

        Parameters
        ----------
        firebase : firebase
            A firebase connection.

        Returns
        -------
        None

    """

    global courses
    obj_key_list = []

    result = firebase.get('/Course', None)

    if result is None:
        return

    for i in result.keys():
        obj_key_list.append(i)

    for i in obj_key_list:
        course = Course()
        course.setId(i)
        course.setKnowledgeAreaId(result[i]['KnowledgeAreaId'])
        course.setCatalogId(result[i]['CatalogId'])
        course.setTitle(result[i]['Name'])
        course.setDescription(result[i]['Description'])
        courses.append(course)


def GetLearningObjectives(firebase: firebase) -> None:
    """

        Get LearningObjectives from the database and insert them into the
        global collection.

        Parameters
        ----------
        firebase : firebase
            A firebase connection.

        Returns
        -------
        None

    """

    global learningObjectives
    obj_key_list = []

    result = firebase.get('/LearningObjective', None)

    if result is None:
        return

    for i in result.keys():
        obj_key_list.append(i)

    for i in obj_key_list:
        lo = LearningObjective()
        lo.setId(i)
        lo.setCourseId(result[i]['CourseId'])
        lo.setText(result[i]['Text'])
        learningObjectives.append(lo)


def writeKnowledgeAreaWorksheets(wb: xlsxwriter.Workbook) -> None:
    """

        Iterate through the global collection of KnowledgeAreas,
        create a worksheet for each, and call method to populate
        the worksheet with courses and learning objectives.

        Parameters
        ----------
        wb : Excel Workbook Object

        Returns
        -------
        None.

    """

    global knowledgeAreas

    for knowledgeArea in knowledgeAreas:
        ws = wb.add_worksheet()
        ws.name = knowledgeArea.getText()
        writeWorksheet(ws, knowledgeArea)


def writeWorksheet(ws, knowledgeArea):
    """

        Iterate through the global collection of KnowledgeAreas
        and write them to a worksheet in an Excel workbook.

        Parameters
        ----------
        ws : Excel Worksheet Object
        knowledgeArea : KnowledgeArea Object

        Returns
        -------
        None.

    """

    global courses
    global learningObjectives

    row = 0
    col = 0

    ws.write(row, col, 'CourseId')
    col += 1

    ws.write(row, col, 'Course')
    col += 1

    ws.write(row, col, 'knowledgeAreaId')
    col += 1

    ws.write(row, col, 'KnowledgeArea')

    row += 1
    col = 0

    knowledgeAreaId = knowledgeArea.getId()

    for course in courses:
        #print("Course {}, {} ".format(course.getTitle(), course.getKnowledgeAreaId()))
        if str(course.getKnowledgeAreaId()) == str(knowledgeAreaId):
            courseId = course.getId()
            if course.getDescription() == "":
                ws.write(row, col, courseId)
                col += 1
                ws.write(row, col, course.getTitle())
                row += 1
                col = 0
                continue
            else:
                for learningObjective in learningObjectives:
                    #print("LearningObjective: {}, {} ".format(learningObjective.getText(), learningObjective.getCourseId()))

                    if str(learningObjective.getCourseId()) == str(courseId):
                        ws.write(row, col, courseId)
                        col += 1
                        ws.write(row, col, course.getTitle())
                        col += 1
                        ws.write(row, col, learningObjective.getId())
                        col += 1
                        ws.write(row, col, learningObjective.getText())
                        row += 1
                        col = 0
                continue


GetKnowledgeAreas(firebase)
GetCourses(firebase)
GetLearningObjectives(firebase)

writeKnowledgeAreaWorksheets(workbook)
workbook.close()
