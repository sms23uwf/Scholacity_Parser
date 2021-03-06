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


firebase = firebase.FirebaseApplication('https://scholacity-org.firebaseio.com/')

knowledgeAreas = []
courses = []
learningObjectives = []

workbook = xlsxwriter.Workbook('../outputs/Course_Catalog_Review.xlsx')
coursesWsRow = 0


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


def GetCourses(firebase: firebase) -> None:
    """

        Get Courses from the database and insert them into the
        global collection.

        :param firebase: A firebase connection

    """

    global courses
    obj_key_list = []

    result = firebase.get('/course', None)

    if result is None:
        return

    for i in result.keys():
        obj_key_list.append(i)

    for i in obj_key_list:
        course = Course()
        course.setId(i)
        course.setKnowledgeAreaId(result[i]['knowledgeareaid'])
        course.setCatalogId(result[i]['catalogid'])
        course.setTitle(result[i]['name'])
        course.setDescription(result[i]['description'])
        courses.append(course)


def GetLearningObjectives(firebase: firebase) -> None:
    """

        Get LearningObjectives from the database and insert them into the
        global collection.

        Parameters
        ----------
        :param firebase: A firebase connection

    """

    global learningObjectives
    obj_key_list = []

    result = firebase.get('/learningobjective', None)

    if result is None:
        return

    for i in result.keys():
        obj_key_list.append(i)

    for i in obj_key_list:
        lo = LearningObjective()
        lo.setId(i)
        lo.setCourseId(result[i]['courseid'])
        lo.setText(result[i]['content'])
        learningObjectives.append(lo)

def writeCourseesWorksheet(wb: xlsxwriter.Workbook) -> None:
    """

        Write a separate worksheet for all courses.

        :param wb: Excel Workbook Object

    """

    global knowledgeAreas
    global coursesWsRow


    ws = wb.add_worksheet()
    ws.name = "Courses"

    row = coursesWsRow
    col = 0

    ws.write(row, col, 'LearningObjective')
    col += 1

    ws.write(row, col, 'CourseId')
    col += 1

    ws.write(row, col, 'CourseTitle - As Extracted')
    col += 1

    ws.write(row, col, 'CourseTitle - As Revised')
    col += 1

    ws.write(row, col, 'CourseDescription - As Extracted')
    col += 1

    ws.write(row, col, 'CourseDescription - As Revised')

    coursesWsRow += 1
    col = 0

    for knowledgeArea in knowledgeAreas:
        writeCourseRows(ws, knowledgeArea)


def writeCourseRows(ws: xlsxwriter.worksheet, knowledgeArea: KnowledgeArea) -> None:
    """

        Write the rows in the courses worksheet for all courses under
        the knowledgearea.

        :param ws: Excel Worksheet Object
        :param knowledgeArea: KnowledgeArea

    """

    global courses
    global coursesWsRow

    col = 0
    knowledgeAreaId = knowledgeArea.getId()

    for course in courses:
        if str(course.getKnowledgeAreaId()) == str(knowledgeAreaId):
            ws.write(coursesWsRow, col, knowledgeArea.getText())
            col += 1

            courseId = course.getId()
            ws.write(coursesWsRow, col, courseId)
            col += 1
            ws.write(coursesWsRow, col, course.getTitle())
            col += 2
            ws.write(coursesWsRow, col, course.getDescription())
            coursesWsRow += 1
            col = 0


def writeKnowledgeAreaWorksheets(wb: xlsxwriter.Workbook) -> None:
    """

        Iterate through the global collection of KnowledgeAreas,
        create a worksheet for each, and call method to populate
        the worksheet with courses and learning objectives.

        :param wb: Excel Workbook Object

    """

    global knowledgeAreas

    for knowledgeArea in knowledgeAreas:
        ws = wb.add_worksheet()
        ws.name = knowledgeArea.getText()[0:31]
        writeWorksheet(ws, knowledgeArea)


def writeWorksheet(ws: xlsxwriter.worksheet, knowledgeArea: KnowledgeArea) -> None:
    """

        Iterate through the global collection of KnowledgeAreas
        and write them to a worksheet in an Excel workbook.

        :param ws: Excel Worksheet Object
        :param knowledgeArea: KnowledgeArea Object

    """

    global courses
    global learningObjectives

    row = 0
    col = 0

    ws.write(row, col, 'CourseId')
    col += 1

    ws.write(row, col, 'CourseTitle - As Extracted')
    col += 1

    ws.write(row, col, 'learningObjectiveId')
    col += 1

    ws.write(row, col, 'learningObjective - As Extracted')
    col += 1

    ws.write(row, col, 'learningObjective - As Revised')

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
                # write another row for the course to allow for 2 learning outcomes
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


if __name__ == "__main__":
    GetKnowledgeAreas(firebase)
    GetCourses(firebase)
    GetLearningObjectives(firebase)

    writeCourseesWorksheet(workbook)
    writeKnowledgeAreaWorksheets(workbook)
    workbook.close()
