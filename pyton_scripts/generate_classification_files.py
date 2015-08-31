#!/usr/bin/python

import os
import sys
import psycopg2
import subprocess
from subprocess import Popen, PIPE

password = sys.argv[1]

execution_options = {1: {'DOCUMENTATION', 'DESIGN', 'DEFECT', 'IMPLEMENTATION', 'TEST', 'WITHOUT_CLASSIFICATION'}, 
                     2: {'DEFECT', 'WITHOUT_CLASSIFICATION'}, 
                     3: {'DESIGN', 'WITHOUT_CLASSIFICATION'}, 
                     4: {'DOCUMENTATION', 'WITHOUT_CLASSIFICATION'}, 
                     5: {'IMPLEMENTATION', 'WITHOUT_CLASSIFICATION'}, 
                     6: {'TEST', 'WITHOUT_CLASSIFICATION'}
}

dataset_directories = {1:'/Users/evermal/git/npl_tools/datasets/all_classes/', 
                       2:'/Users/evermal/git/npl_tools/datasets/defect_vs_without_classification/', 
                       3:'/Users/evermal/git/npl_tools/datasets/design_vs_without_classification/',
                       4:'/Users/evermal/git/npl_tools/datasets/documentation_vs_without_classification/',
                       5:'/Users/evermal/git/npl_tools/datasets/implementation_vs_without_classification/',
                       6:'/Users/evermal/git/npl_tools/datasets/test_vs_without_classification/'
}

test_projects = { 1:'apache-ant-1.7.0',
                  2:'apache-jmeter-2.10',
                  3:'argouml',
                  4:'columba-1.4-src',
                  5:'emf-2.4.1',
                  6:'hibernate-distribution-3.3.2.GA',
                  7:'jEdit-4.2',
                  8:'jfreechart-1.0.19',
                  9:'jruby-1.4.0',
                  10:'sql12'    
}

# create the files used by the stanford classifier, train and test both. 
def write_classifier_file(file_name, result):
    with open (file_name,'a') as classified_seq:
        for line in result:
            classified_seq.write("{0}\t{1}\n".format(line[0], line[1].replace('\n','').replace('\r\n', '').replace('\r', '')))
        classified_seq.close()

def write_output_file(file_name, output):
    with open (file_name,'a') as classified_seq:
        for line in output:
            classified_seq.write(line)
        classified_seq.close()

def write_classifier_properties_file(path):
    f = open(path + "/dataset.prop", "wb")
    f.write("#\n")
    f.write("# Features\n")
    f.write("#\n")
    f.write("useClassFeature=true\n")
    f.write("1.useNGrams=true\n")
    f.write("1.usePrefixSuffixNGrams=true\n")
    f.write("1.maxNGramLeng=4\n")
    f.write("1.minNGramLeng=1\n")
    f.write("1.binnedLengths=10,20,30\n")
    f.write("#\n")
    f.write("# Printing\n")
    f.write("#\n") 
    f.write("printClassifier=HighWeight\n")
    f.write("printClassifierParam=500\n")
    f.write("displayAllAnswers=true\n")
    f.write("printTo="+path+"/top_features.txt\n")
    f.write("#\n")
    f.write("# Mapping\n")
    f.write("#\n")
    f.write("goldAnswerColumn=0\n")
    f.write("displayedColumn=1\n")
    f.write("#\n")
    f.write("# Optimization\n")
    f.write("#\n")
    f.write("intern=true\n")
    f.write("sigma=3\n")
    f.write("useQN=true\n")
    f.write("QNsize=15\n")
    f.write("tolerance=1e-4\n")
    f.write("#\n")
    f.write("# Training input\n")
    f.write("#\n")
    f.write("trainFile="+path+"/classified_seq.train\n")
    f.write("testFile= "+path+"/classified_seq.test\n")
    f.close()

try:
    connection = None

    # connect to the database 
    connection = psycopg2.connect(host='localhost', port='5432', database='comment_classification', user='evermal', password= password)
    cursor = connection.cursor()


    # Choose execution options
    print 'Choose execution mode: \n [1] - All types \n [2] - Defect vs Without classification \n [3] - Design vs Without classification \n [4] - Documentation vs Without classification \n [5] - Implementation vs Without classification \n [6] - Test vs Without classification'
    execution_mode = input()
    print '\n'

    # The process will incrementaly train data based on the order of this input.
    # Each interation increases the amount of data trained by one project, which means that in the last interation the classifier will be trained with all projects in this list. 
    print 'Enter training projects separated by ";"'
    trainig_group = raw_input()
    print '\n'

    print 'Select test project number: ' + str(test_projects)
    test_project = test_projects[input()]
    print '\n'
    
    # Creating test dataset
    for td_type in execution_options[execution_mode]:
        cursor.execute("select a.classification, a.commenttext from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like '%"+test_project+"%' and classification in ('"+td_type+"')")
        write_classifier_file('classified_seq.test', cursor.fetchall())

    # counter that marks the number of projects that is currently used to create the training dataset for the classifier
    number_of_training_projects = 0
    path = dataset_directories[execution_mode] + test_project

    # copy the classifier to the root folder
    subprocess.call(["cp", "/Users/evermal/Documents/stanford-classifier-2015-04-20/stanford-classifier.jar", "./"])

    # create directory based on the name of the tested project.
    # this directory will hold all the other training data for the classifier. the folder 1 means that it was trained with one project, 2 with two projects and so on. 
    subprocess.call(["mkdir", path])
    # create here the readme.md for this folder

    for project in trainig_group.split(';'):
        for td_type in execution_options[execution_mode]:
            # Creating training dataset
            cursor.execute("select a.classification, a.commenttext from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like '%"+project+"%' and classification in ('"+td_type+"')")
            write_classifier_file('classified_seq.train', cursor.fetchall())

        number_of_training_projects = number_of_training_projects + 1
        path_to_store_data = path+"/"+str(number_of_training_projects)
        # create directory equivalent to the number of projects used to train the dataset
        subprocess.call(["mkdir", path_to_store_data])
        # copy files from the root folder to the right one
        subprocess.call(["cp", "classified_seq.train", path_to_store_data])
        subprocess.call(["cp", "classified_seq.test", path_to_store_data])
        write_classifier_properties_file(path_to_store_data) 
        # output = subprocess.check_output(["java -jar stanford-classifier.jar -prop "+path_to_store_data+"/dataset.prop"], stderr=subprocess.STDOUT, shell=True)
        print "Analysis started for " + project
        output = subprocess.Popen(["java -jar stanford-classifier.jar -prop "+path_to_store_data+"/dataset.prop"], stdout=PIPE, stderr=PIPE, shell=True).communicate()
        print "Analysis finished"
        write_output_file(path_to_store_data+"/output.txt",  output[0])
        write_output_file(path_to_store_data+"/results.txt", output[1])
        
    subprocess.call(["rm", "classified_seq.train"])
    subprocess.call(["rm", "classified_seq.test"])
    subprocess.call(["rm", "stanford-classifier.jar"])

except Exception, e:
    print e
    raise e