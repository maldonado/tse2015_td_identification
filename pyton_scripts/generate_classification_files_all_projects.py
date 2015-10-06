#!/usr/bin/python

import os
import sys
import psycopg2
import subprocess
from subprocess import Popen, PIPE

password = sys.argv[1]

execution_options = {
                     # 'DEFECT': {'DEFECT', 'WITHOUT_CLASSIFICATION'}, 
                     'DESIGN': {'DESIGN', 'WITHOUT_CLASSIFICATION'}, 
                     # 'DOCUMENTATION': {'DOCUMENTATION', 'WITHOUT_CLASSIFICATION'}, 
                     'IMPLEMENTATION': {'IMPLEMENTATION', 'WITHOUT_CLASSIFICATION'} 
                     # 'TEST': {'TEST', 'WITHOUT_CLASSIFICATION'}
}

execution_types = {  
                     # 'DEFECT': {'DEFECT'}, 
                     'DESIGN': {'DESIGN'}, 
                     # 'DOCUMENTATION': {'DOCUMENTATION'}, 
                     'IMPLEMENTATION': {'IMPLEMENTATION'}
                     # 'TEST': {'TEST'}
}

dataset_directories = {
                       # 'DEFECT':'/Users/evermal/git/npl_tools/datasets/defect_vs_without_classification/', 
                       'DESIGN':'/Users/evermal/git/npl_tools/datasets/design_vs_without_classification/',
                       # 'DOCUMENTATION':'/Users/evermal/git/npl_tools/datasets/documentation_vs_without_classification/',
                       'IMPLEMENTATION':'/Users/evermal/git/npl_tools/datasets/implementation_vs_without_classification/'
                       # 'TEST':'/Users/evermal/git/npl_tools/datasets/test_vs_without_classification/'
}


# create the files used by the stanford classifier, train and test both. 
def write_classifier_file(file_name, result):
    with open (file_name,'a') as classified_seq:
        for line in result:
            sentence = " ".join(line[1].lower().replace('\n','').replace('\r\n', '').replace('\r', '').replace('\t', '').replace('//','').replace('/**','').replace('*/','').replace('/*','').replace('*','').replace(',','').replace(':','').replace('...','').replace(';','').split())
            if sentence :
                classified_seq.write("{0}\t{1}\n".format(line[0], sentence))
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
    f.write("1.useNGrams=false\n")
    f.write("1.useSplitWords\n") 
    f.write('1.splitWordsRegexp "\s"\n')
    # f.write("useBinary=true\n")
    # f.write("1.usePrefixSuffixNGrams=true\n")
    # f.write("1.maxNGramLeng=4\n")
    # f.write("1.minNGramLeng=1\n")
    f.write("1.binnedLengths=10,20,30\n")
    f.write("#\n")
    f.write("# Printing\n")
    f.write("#\n") 
    f.write("printClassifier=HighWeight\n")
    f.write("printClassifierParam=60000\n")
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
    order = "decrescent/"
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
            cursor.execute("select a.projectname, count(*) from comment_class a , processed_comment b where a.id = b.commentclassid and b.classification = '"+execution_td_type+"' and a.projectname not in ('"+test_project+"') group by 1 order by 2 desc")
            ordered_training_projects = cursor.fetchall();

            # Creating test dataset
            for td_type in execution_options[execution_td_type]:
                cursor.execute("select a.classification, a.commenttext from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like '%"+test_project+"%' and classification in ('"+td_type+"')")
                write_classifier_file('classified_seq.test', cursor.fetchall())
            
            number_of_training_projects = 0
            subprocess.call(["mkdir", dataset_directories[execution_td_type] + order ])
            path = dataset_directories[execution_td_type] + order + test_project

            # copy the classifier to the root folder
            subprocess.call(["cp", "/Users/evermal/Documents/stanford-classifier-2015-04-20/stanford-classifier.jar", "./"])

            # create directory based on the name of the tested project.
            # this directory will hold all the other training data for the classifier. the folder 1 means that it was trained with one project, 2 with two projects and so on. 
            subprocess.call(["mkdir", path])
            # create here the readme.md for this folder

            for project_result in ordered_training_projects:
                project = project_result[0]
                for td_type in execution_options[execution_td_type]:
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
                print "Add comments from " + project + " to training data:"
                print "Start analysis"
                output = subprocess.Popen(['java -mx6144m -jar stanford-classifier.jar -prop '+path_to_store_data+'/dataset.prop -1.useSplitWords -1.splitWordsRegexp "\s"'], stdout=PIPE, stderr=PIPE, shell=True).communicate()
                print "Analysis finished"
                write_output_file(path_to_store_data+"/output.txt",  output[0])
                write_output_file(path_to_store_data+"/results.txt", output[1])
                
            subprocess.call(["rm", "classified_seq.train"])
            subprocess.call(["rm", "classified_seq.test"])
            subprocess.call(["rm", "stanford-classifier.jar"])
            

except Exception, e:
    print e
    raise e