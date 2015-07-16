#!/usr/bin/python

import os
import sys
import psycopg2

password = sys.argv[1]

execution_options = {1: {'DOCUMENTATION', 'DESIGN', 'DEFECT', 'IMPLEMENTATION', 'TEST', 'WITHOUT_CLASSIFICATION'}, 2: {'DEFECT', 'WITHOUT_CLASSIFICATION'}, 3: {'DESIGN', 'WITHOUT_CLASSIFICATION'}, 4: {'DOCUMENTATION', 'WITHOUT_CLASSIFICATION'}, 5: {'IMPLEMENTATION', 'WITHOUT_CLASSIFICATION'}, 6: {'TEST', 'WITHOUT_CLASSIFICATION'}}

def write_in_file(file_name, result):
    with open (file_name,'a') as classified_seq:
        for line in result:
            classified_seq.write("{0}\t{1}\n".format(line[0], line[1].replace('\n','').replace('\r\n', '').replace('\r', '')))
try:
    connection = None

    # connect to the database to retrieve the file name linked with the commit
    connection = psycopg2.connect(host='localhost', port='5432', database='comment_classification', user='evermal', password= password)
    cursor = connection.cursor()

    # Choose execution options
    print 'Choose execution mode: \n [1] - All types \n [2] - Defect vs Without classification \n [3] - Design vs Without classification \n [4] - Documentation vs Without classification \n [5] - Implementation vs Without classification \n [6] - Test vs Without classification'
    execution_mode = input()
    print '\n'

    print 'Enter training projects separated by ";"'
    trainig_group = raw_input()
    print '\n'

    print 'Enter test projects separated by ";"'
    test_group = raw_input()
    print '\n'

    for project in trainig_group.split(';'):

        for td_type in execution_options[execution_mode]:
            # Creating training dataset
            cursor.execute("select a.classification, a.commenttext from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like '%"+project+"%' and classification in ('"+td_type+"')")
            write_in_file('classified_seq.train', cursor.fetchall())

    for project in test_group.split(';'):

        for td_type in execution_options[execution_mode]:
            # Creating test dataset
            cursor.execute("select a.classification, a.commenttext from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like '%"+project+"%' and classification in ('"+td_type+"')")
            write_in_file('classified_seq.test', cursor.fetchall())



except Exception, e:
    raise e