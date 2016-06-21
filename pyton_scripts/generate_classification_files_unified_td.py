#!/usr/bin/python
import os
import sys
import psycopg2
import subprocess
from subprocess import Popen, PIPE

# create the files used by the stanford classifier, train and test both. 
def write_classifier_file(file_name, result):
    with open (file_name,'a') as classified_seq:
        for line in result:
            sentence = " ".join(line[1].lower().replace('\n','').replace('\r\n', '').replace('\r', '').replace('\t', '').replace('//','').replace('/**','').replace('*/','').replace('/*','').replace('*','').replace(',','').replace(':','').replace('...','').replace(';','').split())
            if sentence :
                if 'WITHOUT_CLASSIFICATION' == line[0]:
                    classification = line[0]
                else:
                    classification = 'TECHNICAL_DEBT'
                classified_seq.write("{0}\t{1}\n".format(classification, sentence))
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

connection = psycopg2.connect(host='localhost', port='5432', database='comment_classification', user='evermal', password= '')
cursor = connection.cursor()

dataset_directory = "/Users/evermal/git/tse2015/tse2015_td_identification/datasets/td_vs_nontd/"

cursor.execute("select distinct(projectname) from comment_class order by 1")
test_projects = cursor.fetchall()

# copy the classifier to the root folder
subprocess.call(["cp", "/Users/evermal/Documents/stanford-classifier-2015-04-20/stanford-classifier.jar", "./"])

for test_project_result in test_projects:
    test_project = test_project_result[0]
    print "Project used as test data :" + test_project

    cursor.execute("select a.projectname, count(*) from comment_class a , processed_comment b where a.id = b.commentclassid and b.classification in %s and a.projectname != %s group by 1 order by 2 desc", [tuple([('DESIGN'), ('IMPLEMENTATION')]), test_project])
    ordered_training_projects = cursor.fetchall();

    # Creating test dataset
    subprocess.call(["rm", "classified_seq.test" ])
    subprocess.call(["rm", "classified_seq.train"])     
    cursor.execute("select a.classification, a.commenttext from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like '%"+test_project+"%' and classification in ('DESIGN','IMPLEMENTATION','WITHOUT_CLASSIFICATION') ")
    write_classifier_file('classified_seq.test', cursor.fetchall())

    
    
    number_of_training_projects = 1
    for project_name in ordered_training_projects:
        project = project_name[0]

        # Creating directory 
        directory_path = dataset_directory + test_project +"/"+ str(number_of_training_projects)       
        subprocess.call(["mkdir","-p", directory_path])
        print project

        # Creating training dataset
        cursor.execute("select a.classification, a.commenttext from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like '%"+project+"%' and classification in ('DESIGN','IMPLEMENTATION','WITHOUT_CLASSIFICATION')")
        write_classifier_file('classified_seq.train', cursor.fetchall())

        # copy files from the root folder to the right one
        subprocess.call(["cp", "classified_seq.train", directory_path])
        subprocess.call(["cp", "classified_seq.test",  directory_path])

        write_classifier_properties_file(directory_path)

        print "Start analysis"
        output = subprocess.Popen(['java -mx6144m -jar stanford-classifier.jar -prop '+directory_path+'/dataset.prop -1.useSplitWords -1.splitWordsRegexp "\s"'], stdout=PIPE, stderr=PIPE, shell=True).communicate()
        print "Analysis finished"
    
        write_output_file(directory_path+"/output.txt",  output[0])
        write_output_file(directory_path+"/results.txt", output[1])

        number_of_training_projects = number_of_training_projects + 1 
    
subprocess.call(["rm", "stanford-classifier.jar"])    