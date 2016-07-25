import psycopg2
import timeit
import subprocess
import random
from subprocess import Popen, PIPE

comments_per_iteration = 500

def write_classifier_file(file_name, result):
    with open (file_name,'a') as classified_seq:
        for line in result:
                classified_seq.write("{0}\t{1}\n".format(line[0], line[1]))
        classified_seq.close()

def write_output_file(file_name, output):
    with open (file_name,'a') as classified_seq:
        for line in output:
            classified_seq.write(line)
        classified_seq.close()

def write_classifier_properties_file(path):
    f = open(path + "/dataset.prop", "wb")
    f.write(bytes("#\n",'UTF-8'))
    f.write(bytes("# Features\n",'UTF-8'))
    f.write(bytes("#\n",'UTF-8'))
    f.write(bytes("useClassFeature=true\n",'UTF-8'))
    f.write(bytes("1.useNGrams=false\n",'UTF-8'))
    f.write(bytes("1.useSplitWords\n",'UTF-8'))
    f.write(bytes('1.splitWordsRegexp "\s"\n','UTF-8'))
    f.write(bytes("1.binnedLengths=10,20,30\n",'UTF-8'))
    f.write(bytes("#\n",'UTF-8'))
    f.write(bytes("# Printing\n",'UTF-8'))
    f.write(bytes("#\n",'UTF-8'))
    f.write(bytes("printClassifier=HighWeight\n",'UTF-8'))
    f.write(bytes("printClassifierParam=60000\n",'UTF-8'))
    f.write(bytes("displayAllAnswers=true\n",'UTF-8'))
    f.write(bytes("printTo="+path+"/top_features.txt\n",'UTF-8'))
    f.write(bytes("#\n",'UTF-8'))
    f.write(bytes("# Mapping\n",'UTF-8'))
    f.write(bytes("#\n",'UTF-8'))
    f.write(bytes("goldAnswerColumn=0\n",'UTF-8'))
    f.write(bytes("displayedColumn=1\n",'UTF-8'))
    f.write(bytes("#\n",'UTF-8'))
    f.write(bytes("# Optimization\n",'UTF-8'))
    f.write(bytes("#\n",'UTF-8'))
    f.write(bytes("intern=true\n",'UTF-8'))
    f.write(bytes("sigma=3\n",'UTF-8'))
    f.write(bytes("useQN=true\n",'UTF-8'))
    f.write(bytes("QNsize=15\n",'UTF-8'))
    f.write(bytes("tolerance=1e-4\n",'UTF-8'))
    f.write(bytes("#\n",'UTF-8'))
    f.write(bytes("# Training input\n",'UTF-8'))
    f.write(bytes("#\n",'UTF-8'))
    f.write(bytes("trainFile="+path+"/classified_seq.train\n",'UTF-8'))
    f.write(bytes("testFile= "+path+"/classified_seq.test\n",'UTF-8'))
    f.close()

execution_order = {
                      0: {1,2,3,4,5,6,7,8,9},  
                      1: {0,2,3,4,5,6,7,8,9}, 
                      2: {0,1,3,4,5,6,7,8,9}, 
                      3: {0,1,2,4,5,6,7,8,9}, 
                      4: {0,1,2,3,5,6,7,8,9}, 
                      5: {0,1,2,3,4,6,7,8,9}, 
                      6: {0,1,2,3,4,5,7,8,9}, 
                      7: {0,1,2,3,4,5,6,8,9}, 
                      8: {0,1,2,3,4,5,6,7,9}, 
                      9: {0,1,2,3,4,5,6,7,8}
}

connection = psycopg2.connect(host='localhost', port='5432', database='comment_classification', user='evermal', password= '')
cursor = connection.cursor()


all_design_debt_comments = 0
all_without_classification_comments = 0 


cursor.execute("select classification, treated_commenttext from processed_comment where classification in ('WITHOUT_CLASSIFICATION', 'BUG_FIX') and treated_commenttext != ''")
all_without_classification_comments = cursor.fetchall()
# shuffle the results so the results will not be biased per project (due to the sequential insertion of the files)
random.shuffle(all_without_classification_comments, random.random)
all_without_classification_comments_remainder = len(all_without_classification_comments) % 10

cursor.execute("select classification, treated_commenttext from processed_comment where classification in ('DESIGN') and treated_commenttext != ''")
all_design_debt_comments = cursor.fetchall()
# shuffle the results so the results will not be biased per project (due to the sequential insertion of the files)
random.shuffle(all_design_debt_comments, random.random)
all_design_debt_comments_remainder = len(all_design_debt_comments) % 10

# dividing the dataset into equal parts
divided_dataset = []
for x in range (0,10):
    temp_list = []
    for design_debt_counter in range (0,270):
        temp_list.append(all_design_debt_comments.pop())
        
    for without_classification_counter in range (0,5812):
        temp_list.append(all_without_classification_comments.pop())
    
    #add the remainders in in the last iteration
    if x == 9 : 
        for design_debt_counter in range (0, all_design_debt_comments_remainder):
            temp_list.append(all_design_debt_comments.pop())
        
        for without_classification_counter in range (0, all_without_classification_comments_remainder):
            temp_list.append(all_without_classification_comments.pop())    

    divided_dataset.append(temp_list)


# copy the classifier to the root folder
subprocess.call(["cp", "/Users/evermal/Documents/stanford-classifier-2015-04-20/stanford-classifier.jar", "./"])

for testing_part in execution_order.keys():
    before = timeit.default_timer()
    
    # remove training and test data
    subprocess.call(["rm", "classified_seq.train"])
    subprocess.call(["rm", "classified_seq.test"])
    
    # create folder to store the classification
    current_classification_path = "/Users/evermal/git/tse2015/tse2015_td_identification/datasets/design/ten_folds_validation/"+ str(testing_part)+"/"
    subprocess.call(["mkdir", current_classification_path])

    # create test data for this fold
    testing_data = divided_dataset[testing_part]
    write_classifier_file('classified_seq.test', testing_data)
    
    # creating training dataset progressively while executing the classification 
    total_training_data = []
    for training_index in execution_order[testing_part]:
        total_training_data = total_training_data + divided_dataset[training_index]
    number_of_iterations = int(len(total_training_data) / comments_per_iteration)
    total_training_data_remainder = len(total_training_data) % comments_per_iteration
    
    # balancing the number of comments 
    for iteration_counter in range (0, number_of_iterations):
        writter_buffer = []
        design_added_counter = 0
        for item in total_training_data:
            if item[0] == 'DESIGN':
                writter_buffer.append(total_training_data.pop(total_training_data.index(item)))
                design_added_counter = design_added_counter + 1
            if design_added_counter == 22:
                break
        without_classificaiton_added_counter = 0
        for item in total_training_data:
            if item[0] == 'WITHOUT_CLASSIFICATION':
                writter_buffer.append(total_training_data.pop(total_training_data.index(item)))
                without_classificaiton_added_counter = without_classificaiton_added_counter + 1
            if without_classificaiton_added_counter == 478:
                break
        if iteration_counter == number_of_iterations - 1:
            for training_data_counter in range (0, total_training_data_remainder):
                writter_buffer.append(total_training_data.pop())
        write_classifier_file('classified_seq.train', writter_buffer)

    # without balancing the types of comment
    # for iteration_counter in range (0, number_of_iterations):
    #     writter_buffer = []
    #     for training_data_counter in range (0, comments_per_iteration):

    #         writter_buffer.append(total_training_data.pop())
    #     if iteration_counter == number_of_iterations - 1:
    #         for training_data_counter in range (0, total_training_data_remainder):
    #             writter_buffer.append(total_training_data.pop())

    #     write_classifier_file('classified_seq.train', writter_buffer)

        # defining name of folder that will store the classified results
        if iteration_counter == 0 :
            folder_name = str(comments_per_iteration)
        else:
            folder_name = str((iteration_counter + 1) * comments_per_iteration)
        path_to_store_data = current_classification_path + folder_name

        # setuping necessaries files for the classification
        subprocess.call(["mkdir", path_to_store_data ])
        subprocess.call(["cp", "classified_seq.train", path_to_store_data])
        subprocess.call(["cp", "classified_seq.test", path_to_store_data])
        write_classifier_properties_file(path_to_store_data)

        # executing the classification 
        print("classifying...")
        output = subprocess.Popen(['java -mx6144m -jar stanford-classifier.jar -prop '+path_to_store_data+'/dataset.prop -1.useSplitWords -1.splitWordsRegexp "\s"'], stdout=PIPE, stderr=PIPE, shell=True).communicate()

        write_output_file(path_to_store_data+"/output.txt",  output[0].strip().decode("utf-8"))
        write_output_file(path_to_store_data+"/results.txt", output[1].strip().decode("utf-8"))
        print("done")
        
        print("Fold: ", testing_part, " iteration ", iteration_counter + 1 , " of ", number_of_iterations)

    after = timeit.default_timer()
    print ("total time to process the iteration:", (after - before)/60)

subprocess.call(["rm", "stanford-classifier.jar"])
subprocess.call(["rm", "classified_seq.train"])
subprocess.call(["rm", "classified_seq.test"])