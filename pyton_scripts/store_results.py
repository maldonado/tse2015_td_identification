#!/usr/bin/python

import os
import sys
import psycopg2
import re

password = sys.argv[1]

execution_types = {
                     # 'DEFECT': {'DEFECT'}, 
                     'DESIGN': {'DESIGN'}, 
                     'IMPLEMENTATION': {'IMPLEMENTATION'}
                     
}

dataset_directories = {
                       # 'DEFECT':'/Users/evermal/git/npl_tools/datasets/defect_vs_without_classification/capitalized_training/whole_word/', 
                       'DESIGN':'/Users/evermal/git/npl_tools/datasets/design_vs_without_classification/binary_classifier/',
                       'IMPLEMENTATION':'/Users/evermal/git/npl_tools/datasets/implementation_vs_without_classification/binary_classifier/'
}

try:
    # fill this information before execution
    order = "decrescent/"
    classification_id = '5'
    classification_description = 'classification with whole words as features, training dataset without capital letters and pontuation using binary classifier'

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

    connection = None
    
    # connect to the database 
    connection = psycopg2.connect(host='localhost', port='5432', database='comment_classification', user='evermal', password= password)
    cursor = connection.cursor()

    for key, value in execution_types.iteritems():
        execution_td_type = value.pop()
        print "Running analysis for " + execution_td_type + " vs WITHOUT_CLASSIFICATION:" ;

        cursor.execute("select distinct(projectname) from comment_class order by 1")
        test_projects = cursor.fetchall()

        for test_project_result in test_projects:
            test_project = test_project_result[0]
            print "Project used as test data :" + test_project

            root_dir = dataset_directories[execution_td_type]+order+test_project
            for directory, subdirectory, filelist in os.walk(root_dir):
                current_folder = directory.split('/')[-1] 
                if test_project not in current_folder:
                    opened_file = open(directory+'/results.txt', "r")
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

                    cursor.execute("select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = '"+test_project+"' and a.classification in ('"+execution_td_type+"')")
                    project_classified_comments = cursor.fetchone()[0]

                    cursor.execute("select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = '"+test_project+"' and a.classification in ('WITHOUT_CLASSIFICATION')")
                    project_without_classification_comments = cursor.fetchone()[0]

                    cursor.execute("insert into classifier_results (projectName,classificationid,classificationDescription,category,projectsTrainedWith,totalTrainingComments,withoutClassificationCommentsTrain,classifiedCommentsTrain,totalTestComments,withoutClassificationCommentsTest,classifiedCommentsTest,classifiedTP, classifiedFN,classifiedFP,classifiedTN, classifiedAccuracy,classifiedPrecision,classifiedRecall,classifiedF1,classifiedRandomPrecision,classifiedRandomRecall,classifiedRandomF1,withoutClassificationTP, withoutClassificationFN,withoutClassificationFP,withoutClassificationTN, withoutClassificationAccuracy,withoutClassificationPrecision,withoutClassificationRecall,withoutClassificationF1,withoutClassificatioRandomPrecision,withoutClassificatioRandomRecall,withoutClassificatioRandomF1,microAveragedF1,macroAveragedF1, baselineprecision, baselinerecall, baselinef1) values ('"+test_project+"','"+classification_id+"','"+classification_description+"','"+execution_td_type+"','"+str(current_folder)+"','"+str(total_training_comments)+"','"+str(without_classification_comments)+"','"+str(other_categories_comments)+"','"+str(number_of_comments_test)+"','"+str(project_without_classification_comments)+"','"+str(project_classified_comments)+"','"+str(other_categories_tp)+"','"+str(other_categories_fn)+"','"+str(other_categories_fp)+"','"+str(other_categories_tn)+"','"+str(other_categories_acc)+"','"+str(other_categories_precision)+"','"+str(other_categories_recall)+"','"+str(other_categories_f1)+"','"+str(0.0)+"','"+str(0.0)+"','"+str(0.0)+"','"+str(without_classification_tp)+"','"+str(without_classification_fn)+"','"+str(without_classification_fp)+"','"+str(without_classification_tn)+"','"+str(without_classification_acc)+"','"+str(without_classification_precision)+"','"+str(without_classification_recall)+"','"+str(without_classification_f1)+"','"+str(0.0)+"','"+str(0.0)+"','"+str(0.0)+"','"+str(micro_averaged_f1)+"','"+str(macro_averaged_f1)+"','"+str(0.0)+"','"+str(0.0)+"','"+str(0.0)+"')")
                    print "result inserted"
except Exception, e:
    connection.rollback()
    raise e

finally:
    connection.commit()

                

    