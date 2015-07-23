#!/usr/bin/python

import os
import sys
import psycopg2


password = sys.argv[1]


execution_types = {  
                     'DEFECT': {'DEFECT'}, 
                     'DESIGN': {'DESIGN'}, 
                     'DOCUMENTATION': {'DOCUMENTATION'}, 
                     'IMPLEMENTATION': {'IMPLEMENTATION'}, 
                     'TEST': {'TEST'},
                     'WITHOUT_CLASSIFICATION': {'WITHOUT_CLASSIFICATION'}
}

try:
    connection = None
    
    # connect to the database 
    connection = psycopg2.connect(host='localhost', port='5432', database='comment_classification', user='evermal', password= password)
    cursor = connection.cursor()

    for key, value in execution_types.iteritems():
        execution_td_type = value.pop()

        cursor.execute("select distinct(projectname) from comment_class order by 1")
        test_projects = cursor.fetchall()

        print "calculating for :" + execution_td_type

        with open ("randon_values.md",'a') as output_file:
            output_file.write("## "+ execution_td_type)
            output_file.write("\n")
            output_file.write("|Project                        |  Pr |Rr | F1r |\n")
            output_file.write("|-------------------------------|-----|---|-----|\n")

            for test_project_result in test_projects:
                test_project = test_project_result[0]

                cursor.execute("select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = '"+test_project+"' and a.classification is not null")
                total_comments = cursor.fetchone()
                print total_comments


                cursor.execute("select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = '"+test_project+"' and a.classification in ('"+execution_td_type+"')")
                technical_debt_comments = cursor.fetchone();
                print technical_debt_comments

                if not "WITHOUT_CLASSIFICATION" in execution_td_type :
                    if technical_debt_comments[0] != 0:          
                        randon_precision = float(technical_debt_comments[0]) / float((total_comments[0] - technical_debt_comments[0]))
                        print randon_precision
                        randon_recall = 0.5
                        randon_f1 = ((randon_precision * randon_recall) / (randon_precision + randon_recall)) * 2
                    else:
                        randon_precision = 0.0
                        randon_recall = 0.0
                        randon_f1 = 0.0
                    cursor.execute("update classifier_results set classifiedRandomPrecision = '"+str(round(randon_precision, 3))+"', classifiedRandomRecall = '"+str(round(randon_recall, 3))+"' , classifiedRandomF1 = '"+str(round(randon_f1, 3))+"'  where projectname = '"+test_project+"' and category = '"+execution_td_type+"'")
                else:
                    randon_precision = float(technical_debt_comments[0]) / float((total_comments[0]))
                    print randon_precision
                    randon_recall = 0.5
                    randon_f1 = ((randon_precision * randon_recall) / (randon_precision + randon_recall)) * 2
                    cursor.execute("update classifier_results set withoutclassificatiorandomprecision = '"+str(round(randon_precision, 3))+"', withoutclassificatiorandomrecall = '"+str(round(randon_recall, 3))+"' , withoutclassificatiorandomf1 = '"+str(round(randon_f1, 3))+"'  where projectname = '"+test_project+"'")

                #formating blank spaces
                project_name_blank_spaces = ""
                duration = 32 - len(str(test_project))
                print duration
                for x in xrange(1, duration):
                    project_name_blank_spaces = project_name_blank_spaces + " "

                #formating blank spaces
                precision_blank_spaces = ""
                duration = 6 - len(str(round(randon_precision, 3)))
                for x in xrange(1, duration):
                    precision_blank_spaces = precision_blank_spaces + " "

                #formating blank spaces
                f1_blank_spaces = ""
                duration = 6 - len(str(round(randon_f1, 3)))
                for x in xrange(1, duration):
                    f1_blank_spaces = f1_blank_spaces + " "


                output_file.write("|"+str(test_project)+project_name_blank_spaces+"|"+str(round(randon_precision, 3))+precision_blank_spaces+"|"+str(randon_recall)+"|"+str(round(randon_f1, 3))+f1_blank_spaces+"|\n")

            output_file.write("\n")


except Exception, e:
    print e
    connection.rollback()

finally:
    connection.commit()
    