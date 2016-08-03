#!/usr/bin/python

import os
import sys
import psycopg2
import re





execution_types = {  
                     # 'DEFECT': {'DEFECT'}, 
                     'DESIGN': {'DESIGN'}, 
                     # 'DOCUMENTATION': {'DOCUMENTATION'}, 
                     'IMPLEMENTATION': {'IMPLEMENTATION'}, 
                     # 'TEST': {'TEST'},
                     # 'WITHOUT_CLASSIFICATION': {'WITHOUT_CLASSIFICATION'}
}

try:
    classification_id = '7'

    connection = None
    # connect to the database 
    connection = psycopg2.connect(host='localhost', port='5432', database='comment_classification', user='evermal', password= '')
    cursor = connection.cursor()

    for key, value in execution_types.iteritems():
        execution_td_type = value.pop()

        cursor.execute("select distinct(projectname) from comment_class order by 1")
        test_projects = cursor.fetchall()

        print "calculating for :" + execution_td_type

        for test_project_result in test_projects:
            test_project = test_project_result[0]
            print "project name " + test_project

            cursor.execute("select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = '"+test_project+"' and a.classification is not null")
            total_comments = cursor.fetchone()
            print "total_comments" + str(total_comments)

            cursor.execute("select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = '"+test_project+"' and a.classification in ('"+execution_td_type+"')")
            technical_debt_comments = cursor.fetchone();
            
            print "technical_debt_comments " + str(technical_debt_comments )

            if not "WITHOUT_CLASSIFICATION" in execution_td_type :
                if technical_debt_comments[0] != 0:          
                    randon_precision = float(technical_debt_comments[0]) / float(total_comments[0])
                    # randon_precision = float(technical_debt_comments[0]) / float((total_comments[0] - technical_debt_comments[0]))
                    # print randon_precision
                    randon_recall = 0.5
                    randon_f1 = ((randon_precision * randon_recall) / (randon_precision + randon_recall)) * 2
                else:
                    randon_precision = 0.0
                    randon_recall = 0.0
                    randon_f1 = 0.0

                technical_debt_regex = 'hack|retarded|at\sa\sloss|stupid|remove\sthis\scode|ugly|take\scare|something.s\sgone\swrong|nuke|is\sproblematic|may\scause\sproblem|hacky|unknown\swhy\swe\sever\sexperience\sthis|treat\sthis\sas\sa\ssoft\serror|silly|workaround\sfor\sbug|kludge|fixme|this\sisn.t\squite\sright|trial\sand\serror|give\sup|this\sis\swrong|hang\sour\sheads\sin\sshame|temporary\ssolution|causes\sissue|something\sbad\sis\sgoing\son|cause\sfor\sissue|this\sdoesn.t\slook\sright|is\sthis\snext\sline\ssafe|this\sindicates\sa\smore\sfundamental\sproblem|temporary\scrutch|this\scan\sbe\sa\smess|this\sisn.t\svery\ssolid|this\sis\stemporary\sand\swill\sgo\saway|is\sthis\sline\sreally\ssafe|there\sis\sa\sproblem|some\sfatal\serror|something\sserious\sis\swrong|don.t\suse\sthis|get\srid\sof\sthis|doubt\sthat\sthis\swould\swork|this\sis\sbs|give\sup\sand\sgo\saway|risk\sof\sthis\sblowing\sup|just\sabandon\sit|prolly\sa\sbug|probably\sa\sbug|hope\severything\swill\swork|toss\sit|barf|something\sbad\shappened|fix\sthis\scrap|yuck|certainly\sbuggy|remove\sme\sbefore\sproduction|you\scan\sbe\sunhappy\snow|this\sis\suncool|bail\sout|it\sdoesn.t\swork\syet|crap|inconsistency|abandon\sall\shope|kaboom'
                td_counter = 0 
                false_positive = 0
                true_positive = 0
                true_negative = 0
                false_negative = 0
                recall = 0.000
                precision = 0.000
                f1measure = 0.000

                cursor.execute("select a.treated_commenttext, a.classification from processed_comment a , comment_class b where a.commentclassid= b.id and a.classification in ('"+execution_td_type+"', 'WITHOUT_CLASSIFICATION','BUG_FIX_COMMENT') and b.projectname like '%"+test_project+"%'")
                # cursor.execute("select a.commenttext, a.classification from processed_comment a , comment_class b where a.commentclassid= b.id and b.projectname like '%"+test_project+"%'")
                comments = cursor.fetchall()

                for comment in comments:
                    match = re.search(technical_debt_regex, comment[0])
                    if match:
                        td_counter = td_counter + 1
                        if comment[1] == 'WITHOUT_CLASSIFICATION' or comment[1] == 'BUG_FIX_COMMENT':
                            false_positive = false_positive + 1
                        else:
                            true_positive = true_positive + 1
                    else:
                        if comment[1] == 'WITHOUT_CLASSIFICATION' or comment[1] == 'BUG_FIX_COMMENT':
                            true_negative = true_negative + 1
                        else:
                            false_negative = false_negative + 1
                if true_positive != 0:
                    recall = float(true_positive) / float((true_positive + false_negative))
                    precision = float(true_positive) / float((true_positive + false_positive))
                    f1measure = ((precision * recall) / (precision + recall)) * 2

                print "first case"
                print "randon_recall:"+str(randon_recall)
                print "randon_precision:"+str(randon_precision)
                print "randon_f1:"+str(randon_f1)
                print "-------"
                print "rounded randon_recall:"+str(round(randon_recall, 3))
                print "rounded randon_precision:"+str(round(randon_precision, 3))
                print "rounded randon_f1:"+str(round(randon_f1, 3))
                cursor.execute("update classifier_results set classifiedRandomPrecision = '"+str(round(randon_precision, 3))+"', classifiedRandomRecall = '"+str(round(randon_recall, 3))+"' , classifiedRandomF1 = '"+str(round(randon_f1, 3))+"', baselineprecision = '"+str(round(precision, 3))+"', baselinerecall = '"+str(round(recall, 3))+"' , baselinef1 = '"+str(round(f1measure, 3))+"'  where projectname = '"+test_project+"' and category = '"+execution_td_type+"' and classificationid = " + classification_id ) 

            else:
                randon_precision = float(technical_debt_comments[0]) / float((total_comments[0]))
                print randon_precision
                randon_recall = 0.5
                randon_f1 = ((randon_precision * randon_recall) / (randon_precision + randon_recall)) * 2
                
                print "second case"
                print "randon_recall"+str(randon_recall)
                print "randon_precision"+str(randon_precision)
                print "randon_f1"+str(randon_f1)
                print "-------"
                print "randon_recall"+str(round(randon_recall, 3))
                print "randon_precision"+str(round(randon_precision, 3))
                print "randon_f1"+str(round(randon_f1, 3))
                cursor.execute("update classifier_results set withoutclassificatiorandomprecision = '"+str(round(randon_precision, 3))+"', withoutclassificatiorandomrecall = '"+str(round(randon_recall, 3))+"' , withoutclassificatiorandomf1 = '"+str(round(randon_f1, 3))+"'  where projectname = '"+test_project+"' and classificationid = "+classification_id)
                
except Exception, e:
    print e
    connection.rollback()

finally:
    # pass
    connection.commit()