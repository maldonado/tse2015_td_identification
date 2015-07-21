#!/usr/bin/python

import os
import sys
import psycopg2

test_project = sys.argv[1]
train_project_1 = sys.argv[2]
train_project_2 = sys.argv[3]
train_project_3 = sys.argv[4]
train_project_4 = sys.argv[5]

password = sys.argv[6]

def write_in_file(file_name, result):
    with open (file_name,'a') as classified_seq:
        for line in result:
            classified_seq.write("{0}\t{1}\n".format(line[0], line[1].replace('\n','').replace('\r\n', '').replace('\r', '')))

try:

    connection = None
    
    # connect to the database to retrieve the file name linked with the commit
    connection = psycopg2.connect(host='localhost', port='5432', database='comment_classification', user='evermal', password= password)
    cursor = connection.cursor()
 
    # Creating training dataset
    cursor.execute("select a.classification, a.commenttext from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like '%"+train_project_1+"%' and classification not in ('BUG_FIX_COMMENT')")
    write_in_file('classified_seq.train', cursor.fetchall())

    cursor.execute("select a.classification, a.commenttext from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like '%"+train_project_2+"%' and classification not in ('BUG_FIX_COMMENT')")
    write_in_file('classified_seq.train', cursor.fetchall())

    cursor.execute("select a.classification, a.commenttext from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like '%"+train_project_3+"%' and classification not in ('BUG_FIX_COMMENT')")
    write_in_file('classified_seq.train', cursor.fetchall())

    cursor.execute("select a.classification, a.commenttext from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like '%"+train_project_4+"%' and classification not in ('BUG_FIX_COMMENT')")
    write_in_file('classified_seq.train', cursor.fetchall())

    # Creating test dataset
    cursor.execute("select a.classification, a.commenttext from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like '%"+test_project+"%'  and a.classification in ('DOCUMENTATION') order by 2 ")
    write_in_file('classified_seq.test', cursor.fetchall())

    cursor.execute("select a.classification, a.commenttext from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like '%"+test_project+"%'  and a.classification in ('DESIGN') order by 2 ")
    write_in_file('classified_seq.test', cursor.fetchall())

    cursor.execute("select a.classification, a.commenttext from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like '%"+test_project+"%'  and a.classification in ('DEFECT') order by 2")
    write_in_file('classified_seq.test', cursor.fetchall())

    cursor.execute("select a.classification, a.commenttext from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like '%"+test_project+"%'  and a.classification in ('IMPLEMENTATION') order by 2")
    write_in_file('classified_seq.test', cursor.fetchall())

    cursor.execute("select a.classification, a.commenttext from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like '%"+test_project+"%'  and a.classification in ('TEST') order by 2")
    write_in_file('classified_seq.test', cursor.fetchall())

    cursor.execute("select a.classification, a.commenttext from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like '%"+test_project+"%'  and a.classification in ('WITHOUT_CLASSIFICATION') order by 2")
    write_in_file('classified_seq.test', cursor.fetchall())

except Exception, e:
    raise e