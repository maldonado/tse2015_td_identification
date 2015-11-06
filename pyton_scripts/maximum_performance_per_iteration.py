#!/usr/bin/python

import os
import sys
import psycopg2

import re


password = sys.argv[1]



connection = None

classificationid = 7
category =  'IMPLEMENTATION'

# connect to the database 
connection = psycopg2.connect(host='localhost', port='5432', database='comment_classification', user='evermal', password= password)
cursor = connection.cursor()

cursor.execute("select distinct(projectname) from classifier_results order by 1")
projects_results = cursor.fetchall()


for line in projects_results:
    project_name = line[0]
    print "Analyzing project :" + project_name
    
    cursor.execute("select projectstrainedwith, classifiedf1, classifiedCommentsTrain from classifier_results where classificationid= "+str(classificationid)+" and category = '"+category+"' and projectname = '"+project_name+"' order by 2  desc")
    performance_per_iteration_results = cursor.fetchall()

    first_iteration = True
    for iteration in performance_per_iteration_results:
        projectstrainedwith = iteration[0]
        classifiedf1 = iteration[1]
        totalTrainingComments = iteration[2]
        if first_iteration:
            best_performance = classifiedf1
            first_iteration = False
        
        percentage_of_maximum_performance = float(classifiedf1) / float(best_performance)
        print percentage_of_maximum_performance
        
        # uncomment these lines to insert the values in the table.
        cursor.execute("insert into performance_per_iteration (classificationid, category, projectname, projectstrainedwith, totalTrainingComments,  classifiedF1, percentage_of_maximum_performance) values ('"+str(classificationid)+"', '"+category+"', '"+project_name+"', '"+str(projectstrainedwith)+"', '"+str(totalTrainingComments)+"',  '"+str(classifiedf1)+"', '"+str(round(percentage_of_maximum_performance, 3))+"')")
        connection.commit()


for x in xrange(1,10):
    cursor.execute("select percentage_of_maximum_performance, totalTrainingComments from performance_per_iteration where category = '"+category+"' and classificationid = '"+str(classificationid)+"' and projectstrainedwith = "+str(x))
    iteration_performance_result = cursor.fetchall()

    iteration_percentage_of_maximum_performance_sum = 0.0
    iteration_comments_sum = 0

    for iteration_performance in iteration_performance_result:
        iteration_percentage_of_maximum_performance_sum = float(iteration_percentage_of_maximum_performance_sum) + float(iteration_performance[0])
        iteration_comments_sum = iteration_comments_sum + iteration_performance[1]

    iteration_average = float(iteration_percentage_of_maximum_performance_sum) / float(10)
    comments_average  = iteration_comments_sum / 10 
    
    print str(x) +" . "+str(iteration_average)+" . "+str(comments_average)

