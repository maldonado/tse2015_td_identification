# python 3

import numpy
import decimal
import psycopg2

# fill this information before execution
classificationid = '3'
new_classificationid = '5' 
projectname = 'average_classificationid_3'
category = 'DESIGN'

# connect to the database 
connection = psycopg2.connect(host='localhost', port='5432', database='comment_classification', user='evermal', password= '')
cursor = connection.cursor()

cursor.execute("select distinct(projectsTrainedWith) from classifier_results_ten_fold where classificationid = %s", (classificationid,))
projects_trained_with_results = cursor.fetchall()

for number_of_comments in projects_trained_with_results:
    number_of_comment = number_of_comments[0]

    cursor.execute("select classifiedTP from classifier_results_ten_fold where classificationid = %s and projectsTrainedWith = %s", (classificationid, number_of_comment))
    classifiedTP = numpy.average(cursor.fetchall())
    cursor.execute("select classifiedFN from classifier_results_ten_fold where classificationid = %s and projectsTrainedWith = %s", (classificationid, number_of_comment))
    classifiedFN = numpy.average(cursor.fetchall())
    cursor.execute("select classifiedFP from classifier_results_ten_fold where classificationid = %s and projectsTrainedWith = %s", (classificationid, number_of_comment))
    classifiedFP = numpy.average(cursor.fetchall())
    cursor.execute("select classifiedTN from classifier_results_ten_fold where classificationid = %s and projectsTrainedWith = %s", (classificationid, number_of_comment))
    classifiedTN = numpy.average(cursor.fetchall())
    cursor.execute("select classifiedAccuracy from classifier_results_ten_fold where classificationid = %s and projectsTrainedWith = %s", (classificationid, number_of_comment))
    classifiedAccuracy = float(sum(numpy.asarray(cursor.fetchall()))/ 10 )
    cursor.execute("select classifiedPrecision from classifier_results_ten_fold where classificationid = %s and projectsTrainedWith = %s", (classificationid, number_of_comment))
    classifiedPrecision = float(sum(numpy.asarray(cursor.fetchall()))/ 10)
    cursor.execute("select classifiedRecall from classifier_results_ten_fold where classificationid = %s and projectsTrainedWith = %s", (classificationid, number_of_comment))
    classifiedRecall = float(sum(numpy.asarray(cursor.fetchall()))/ 10)
    cursor.execute("select classifiedF1 from classifier_results_ten_fold where classificationid = %s and projectsTrainedWith = %s", (classificationid, number_of_comment))
    classifiedF1 = float(sum(numpy.asarray(cursor.fetchall()))/ 10)
    cursor.execute("select withoutClassificationTP from classifier_results_ten_fold where classificationid = %s and projectsTrainedWith = %s", (classificationid, number_of_comment))
    withoutClassificationTP = numpy.average(cursor.fetchall())
    cursor.execute("select withoutClassificationFN from classifier_results_ten_fold where classificationid = %s and projectsTrainedWith = %s", (classificationid, number_of_comment))
    withoutClassificationFN = numpy.average(cursor.fetchall())
    cursor.execute("select withoutClassificationFP from classifier_results_ten_fold where classificationid = %s and projectsTrainedWith = %s", (classificationid, number_of_comment))
    withoutClassificationFP = numpy.average(cursor.fetchall())
    cursor.execute("select withoutClassificationTN from classifier_results_ten_fold where classificationid = %s and projectsTrainedWith = %s", (classificationid, number_of_comment))
    withoutClassificationTN = numpy.average(cursor.fetchall())
    cursor.execute("select withoutClassificationAccuracy from classifier_results_ten_fold where classificationid = %s and projectsTrainedWith = %s", (classificationid, number_of_comment))
    withoutClassificationAccuracy = float(sum(numpy.asarray(cursor.fetchall())) / 10)
    cursor.execute("select withoutClassificationPrecision from classifier_results_ten_fold where classificationid = %s and projectsTrainedWith = %s", (classificationid, number_of_comment))
    withoutClassificationPrecision = float(sum(numpy.asarray(cursor.fetchall())) / 10)
    cursor.execute("select withoutClassificationRecall from classifier_results_ten_fold where classificationid = %s and projectsTrainedWith = %s", (classificationid, number_of_comment))
    withoutClassificationRecall = float(sum(numpy.asarray(cursor.fetchall())) / 10)
    cursor.execute("select withoutClassificationF1 from classifier_results_ten_fold where classificationid = %s and projectsTrainedWith = %s", (classificationid, number_of_comment))
    withoutClassificationF1 = float(sum(numpy.asarray(cursor.fetchall())) / 10)
    cursor.execute("select microAveragedF1 from classifier_results_ten_fold where classificationid = %s and projectsTrainedWith = %s", (classificationid, number_of_comment))
    microAveragedF1 = float(sum(numpy.asarray(cursor.fetchall())) / 10)
    cursor.execute("select macroAveragedF1 from classifier_results_ten_fold where classificationid = %s and projectsTrainedWith = %s", (classificationid, number_of_comment))
    macroAveragedF1 = float(sum(numpy.asarray(cursor.fetchall())) / 10)

    # print(classifiedTP)
    # print(classifiedFN)
    # print(classifiedFP)
    # print(classifiedTN)
    # print(classifiedAccuracy)
    # print(classifiedPrecision)
    # print(classifiedRecall)
    # print(classifiedF1)
    # print(withoutClassificationTP)
    # print(withoutClassificationFN)
    # print(withoutClassificationFP)
    # print(withoutClassificationTN)
    # print(withoutClassificationAccuracy)
    # print(withoutClassificationPrecision)
    # print(withoutClassificationRecall)
    # print(withoutClassificationF1)
    # print(microAveragedF1)
    # print(macroAveragedF1)
    cursor.execute("insert into classifier_results_ten_fold (projectname, classificationid, projectsTrainedWith, category, classifiedTP, classifiedFN, classifiedFP, classifiedTN, classifiedAccuracy, classifiedPrecision, classifiedRecall, classifiedF1, withoutClassificationTP, withoutClassificationFN, withoutClassificationFP, withoutClassificationTN, withoutClassificationAccuracy, withoutClassificationPrecision, withoutClassificationRecall, withoutClassificationF1, microAveragedF1, macroAveragedF1) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (projectname, new_classificationid, number_of_comment, category,classifiedTP, classifiedFN, classifiedFP, classifiedTN, classifiedAccuracy, classifiedPrecision, classifiedRecall, classifiedF1, withoutClassificationTP, withoutClassificationFN, withoutClassificationFP, withoutClassificationTN, withoutClassificationAccuracy, withoutClassificationPrecision, withoutClassificationRecall, withoutClassificationF1, microAveragedF1, macroAveragedF1))                                                        
    connection.commit()