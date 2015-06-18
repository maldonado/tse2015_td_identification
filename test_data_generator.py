#!/usr/bin/python

import os
import sys
import psycopg2

# database = sys.argv[2]
# password = sys.argv[1]

def write_in_file(result):
    with open ('classified_seq.test','a') as classified_seq:
        for line in result:
            classified_seq.write("{0}\t{1}\n".format(line[0], line[1].replace('\n','')))

try:
    connection = None
    
    # connect to the database to retrieve the file name linked with the commit
    connection = psycopg2.connect(host='localhost', port='5432', database='comment_classification', user='evermal', password= '')
    cursor = connection.cursor()
 
    cursor.execute("select a.classification, a.commenttext from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like '%argouml%'  and a.classification in ('DOCUMENTATION') order by 2 ")
    write_in_file(cursor.fetchall())

    cursor.execute("select a.classification, a.commenttext from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like '%argouml%'  and a.classification in ('DESIGN') order by 2 ")
    write_in_file(cursor.fetchall())

    cursor.execute("select a.classification, a.commenttext from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like '%argouml%'  and a.classification in ('DEFECT') order by 2")
    write_in_file(cursor.fetchall())

    cursor.execute("select a.classification, a.commenttext from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like '%argouml%'  and a.classification in ('IMPLEMENTATION') order by 2")
    write_in_file(cursor.fetchall())

    cursor.execute("select a.classification, a.commenttext from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like '%argouml%'  and a.classification in ('TEST') order by 2")
    write_in_file(cursor.fetchall())

    cursor.execute("select a.classification, a.commenttext from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like '%argouml%'  and a.classification in ('WITHOUT_CLASSIFICATION') order by 2")
    write_in_file(cursor.fetchall())

    cursor.execute("select a.classification, a.commenttext from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like '%argouml%'  and a.classification in ('BUG_FIX_COMMENT') order by 2")
    write_in_file(cursor.fetchall())

except Exception, e:
    raise e