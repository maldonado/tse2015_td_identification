#python 2

import re
import os
import sys
import psycopg2
import random 
import numpy


# parameters
# design_debt = 270
# requirement_debt = 75
# not_design_debt = 5812

# design
number_of_td_comments_per_fold = 270
number_of_not_td_comments_per_fold = 5812

# requirement
# number_of_td_comments_per_fold = 75
# number_of_not_td_comments_per_fold = 5812

# comment pattern regex
technical_debt_regex = 'hack|retarded|at\sa\sloss|stupid|remove\sthis\scode|ugly|take\scare|something.s\sgone\swrong|nuke|is\sproblematic|may\scause\sproblem|hacky|unknown\swhy\swe\sever\sexperience\sthis|treat\sthis\sas\sa\ssoft\serror|silly|workaround\sfor\sbug|kludge|fixme|this\sisn.t\squite\sright|trial\sand\serror|give\sup|this\sis\swrong|hang\sour\sheads\sin\sshame|temporary\ssolution|causes\sissue|something\sbad\sis\sgoing\son|cause\sfor\sissue|this\sdoesn.t\slook\sright|is\sthis\snext\sline\ssafe|this\sindicates\sa\smore\sfundamental\sproblem|temporary\scrutch|this\scan\sbe\sa\smess|this\sisn.t\svery\ssolid|this\sis\stemporary\sand\swill\sgo\saway|is\sthis\sline\sreally\ssafe|there\sis\sa\sproblem|some\sfatal\serror|something\sserious\sis\swrong|don.t\suse\sthis|get\srid\sof\sthis|doubt\sthat\sthis\swould\swork|this\sis\sbs|give\sup\sand\sgo\saway|risk\sof\sthis\sblowing\sup|just\sabandon\sit|prolly\sa\sbug|probably\sa\sbug|hope\severything\swill\swork|toss\sit|barf|something\sbad\shappened|fix\sthis\scrap|yuck|certainly\sbuggy|remove\sme\sbefore\sproduction|you\scan\sbe\sunhappy\snow|this\sis\suncool|bail\sout|it\sdoesn.t\swork\syet|crap|inconsistency|abandon\sall\shope|kaboom'

# database connection
connection = psycopg2.connect(host='localhost', port='5432', database='comment_classification', user='evermal', password= '')
cursor = connection.cursor()

all_design_debt_comments = 0
all_without_classification_comments = 0 

cursor.execute("select classification, commenttext from processed_comment where classification in ('WITHOUT_CLASSIFICATION', 'BUG_FIX') and treated_commenttext != ''")
all_without_classification_comments = cursor.fetchall()
# shuffle the results so the results will not be biased per project (due to the sequential insertion of the files)
random.shuffle(all_without_classification_comments, random.random)
all_without_classification_comments_remainder = len(all_without_classification_comments) % 10

cursor.execute("select classification, commenttext from processed_comment where classification in ('DESIGN') and treated_commenttext != ''")
all_design_debt_comments = cursor.fetchall()
# shuffle the results so the results will not be biased per project (due to the sequential insertion of the files)
random.shuffle(all_design_debt_comments, random.random)
all_techncial_debt_comments_remainder = len(all_design_debt_comments) % 10

# cursor.execute("select classification, commenttext from processed_comment where classification in ('IMPLEMENTATION') and treated_commenttext != ''")
# all_design_debt_comments = cursor.fetchall()
# # shuffle the results so the results will not be biased per project (due to the sequential insertion of the files)
# random.shuffle(all_design_debt_comments, random.random)
# all_techncial_debt_comments_remainder = len(all_design_debt_comments) % 10


# dividing the dataset into equal parts
divided_dataset = []
for x in xrange (0,10):
    temp_list = []
    for technical_debt_counter in xrange (0, number_of_td_comments_per_fold):
        temp_list.append(all_design_debt_comments.pop())
        
    for without_classification_counter in xrange (0, number_of_not_td_comments_per_fold):
        temp_list.append(all_without_classification_comments.pop())
    
    #add the remainders in in the last iteration
    if x == 9 : 
        for technical_debt_counter in range (0, all_techncial_debt_comments_remainder):
            temp_list.append(all_design_debt_comments.pop())
        
        for without_classification_counter in range (0, all_without_classification_comments_remainder):
            temp_list.append(all_without_classification_comments.pop())    

    divided_dataset.append(temp_list)

true_positive_list = []
true_negative_list = []
false_positive_list = []
false_negative_list = []

for test_chunk in divided_dataset:

    print '----------------------------------------------'
    td_counter = 0 
    false_positive = 0
    true_positive = 0
    true_negative = 0
    false_negative = 0
    recall = 0.000
    precision = 0.000
    f1measure = 0.000

    for comment in test_chunk:
        match = re.search(technical_debt_regex, comment[1])
        if match:
            td_counter = td_counter + 1
            if comment[0] == 'WITHOUT_CLASSIFICATION' or comment[0] == 'BUG_FIX_COMMENT':
                false_positive = false_positive + 1
            else:
                true_positive = true_positive + 1
        else:
            if comment[0] == 'WITHOUT_CLASSIFICATION' or comment[0] == 'BUG_FIX_COMMENT':
                true_negative = true_negative + 1
            else:
                false_negative = false_negative + 1


    recall = float(true_positive)     / float((true_positive + false_negative))
    precision = float(true_positive)  / float((true_positive + false_positive))
    f1measure = ((precision * recall) / (precision + recall)) * 2
    
    print 'Precision:  ' + str(precision)
    print 'Recall:     ' + str(recall)
    print 'F1 measure: ' +str (f1measure)

    print 'Total td found: '+str(td_counter)
    print 'True positives: '+str(true_positive)
    print 'True negatives: '+str(true_negative)
    print 'False positives: '+str(false_positive)
    print 'False negatives: '+str(false_negative)


    true_positive_list.append (true_positive) 
    true_negative_list.append (true_negative) 
    false_positive_list.append(false_positive)
    false_negative_list.append(false_negative)

print '-----------Average---------------'

average_true_positive  = numpy.average(true_positive_list)
average_true_negative  = numpy.average(true_negative_list)
average_false_positive = numpy.average(false_positive_list)
average_false_negative = numpy.average(false_negative_list)

average_recall =    float(average_true_positive)  / float((average_true_positive + average_false_negative))
average_precision = float(average_true_positive)  / float((average_true_positive + average_false_positive))
average_f1measure = ((average_precision * average_recall) / (average_precision + average_recall)) * 2
    
print 'Precision:  ' + str(average_precision)
print 'Recall:     ' + str(average_recall)
print 'F1 measure: ' + str(average_f1measure)

print 'True positives: '+str(average_true_positive)
print 'True negatives: '+str(average_true_negative)
print 'False positives: '+str(average_false_positive)
print 'False negatives: '+str(average_false_negative)

print '----------random baseline-------------'

print 'design'
number_of_design_debt = 2703
number_of_non_debt    = 58122
total_number_of_comments = 60825

randon_precision = float(number_of_design_debt) / float((total_number_of_comments - number_of_design_debt))
print randon_precision
randon_recall = 0.5
print randon_recall
randon_f1 = ((randon_precision * randon_recall) / (randon_precision + randon_recall)) * 2
print randon_f1

print 'requirement'

number_of_requirement_debt = 757
number_of_non_debt    = 58122
total_number_of_comments = 58879

randon_precision = float(number_of_requirement_debt) / float((total_number_of_comments - number_of_requirement_debt))
print randon_precision
randon_recall = 0.5
print randon_recall
randon_f1 = ((randon_precision * randon_recall) / (randon_precision + randon_recall)) * 2
print randon_f1