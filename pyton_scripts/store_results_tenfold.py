# python 2

import os
import sys
import psycopg2
import re


# fill this information before execution
classification_id = '3'
classification_description = 'classification with right ratio of design and non design debt comments. Comments added 500 per time'
repository_path = '/Users/evermal/git/tse2015/tse2015_td_identification/datasets/design/ten_folds_validation/03-ratio_training_500x/'
execution_td_type = 'DESIGN'

# getting training dataset numbers
coments_in_training_data_regex = "(?:numDatums:\s)(\d*)?"
without_classification_regex = "(?:WITHOUT\_CLASSIFICATION=)(\d*)?"
other_categories_regex = "(?:DEFECT=|IMPLEMENTATION=|DESIGN=|DOCUMENTATION=|TEST=)(\d*)?"

# number of comments in the test project
number_of_comments_test_data_regex = "(\d*)?(?:\sexamples\sin\stest)"

# results regex
without_classification_results_regex = "(?:Cls\sW.*:\sTP=)(\d*)?(?:\sFN=)(\d*)?(?:\sFP=)(\d*)?(?:\sTN=)(\d*)?(?:.*Acc\s)(\d*\.?\d+)?(?:.*P\s)(\d*\.?\d+)?(?:.*R\s)(\d*\.?\d+)?(?:.*F1\s)(\d*\.?\d+)?" 
other_categories_results_regex = "(?:Cls\s(?:D|I|T).*:\sTP=)(\d*)?(?:\sFN=)(\d*)?(?:\sFP=)(\d*)?(?:\sTN=)(\d*)?(?:.*Acc\s)(\d*\.?\d+)?(?:.*P\s)(\d*\.?\d+)?(?:.*R\s)(\d*\.?\d+)?(?:.*F1\s)(\d*\.?\d+)?"
micro_averaged_f1_regex = "(?:Accuracy.*:\s)(\d*\.?\d+)"
macro_averaged_f1_regex = "(?:Macro.*:\s)(\d*\.?\d+)"

# connect to the database 
connection = psycopg2.connect(host='localhost', port='5432', database='comment_classification', user='evermal', password= '')
cursor = connection.cursor()

for root, dirs, files in os.walk(repository_path):
    for file in files:
        if file == 'results.txt' :
            absolute_path = os.path.join(root, file).replace(repository_path + '/', '')
            projectName = absolute_path.split('/')[-3]
            projectsTrainedWith = absolute_path.split('/')[-2]
            

            opened_file = open(absolute_path, "r")
            for line in opened_file:
                match = re.search(coments_in_training_data_regex, line)
                if match:
                    total_training_comments = match.group(1)
                match = re.search(without_classification_regex, line)
                if match:
                    without_classification_comments = match.group(1)
                match = re.search(other_categories_regex, line)
                if match:
                    other_categories_comments = match.group(1)
                match = re.search(number_of_comments_test_data_regex, line)
                if match:
                    number_of_comments_test = match.group(1)
                match = re.search(without_classification_results_regex, line)
                if match:
                    without_classification_tp = match.group(1)
                    without_classification_fn = match.group(2)
                    without_classification_fp = match.group(3)
                    without_classification_tn = match.group(4)
                    without_classification_acc = match.group(5)
                    without_classification_precision = match.group(6)
                    without_classification_recall = match.group(7)
                    without_classification_f1 = match.group(8)
                match = re.search(other_categories_results_regex, line)
                if match:
                    other_categories_tp = match.group(1)
                    other_categories_fn = match.group(2)
                    other_categories_fp = match.group(3)
                    other_categories_tn = match.group(4)
                    other_categories_acc = match.group(5)
                    other_categories_precision = match.group(6)
                    other_categories_recall = match.group(7)
                    other_categories_f1 = match.group(8)
                match = re.search(micro_averaged_f1_regex, line)
                if match:
                    micro_averaged_f1 = match.group(1)
                match = re.search(macro_averaged_f1_regex, line)
                if match:
                    macro_averaged_f1 = match.group(1)

            cursor.execute("insert into classifier_results_ten_fold (projectName, classificationid, classificationDescription, category, projectsTrainedWith, totalTrainingComments, withoutClassificationCommentsTrain, classifiedCommentsTrain, totalTestComments, classifiedTP, classifiedFN, classifiedFP, classifiedTN, classifiedAccuracy, classifiedPrecision, classifiedRecall, classifiedF1, withoutClassificationTP, withoutClassificationFN, withoutClassificationFP, withoutClassificationTN, withoutClassificationAccuracy, withoutClassificationPrecision, withoutClassificationRecall, withoutClassificationF1, microAveragedF1, macroAveragedF1) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (projectName, classification_id, classification_description, execution_td_type, projectsTrainedWith, total_training_comments,without_classification_comments, other_categories_comments,number_of_comments_test,other_categories_tp, other_categories_fn, other_categories_fp, other_categories_tn,other_categories_acc,other_categories_precision,other_categories_recall,other_categories_f1, without_classification_tp,without_classification_fn,without_classification_fp,without_classification_tn,without_classification_acc, without_classification_precision,without_classification_recall,without_classification_f1,micro_averaged_f1, macro_averaged_f1)) 
            connection.commit()
            print "result inserted"