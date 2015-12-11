#!/usr/bin/python

import psycopg2


# connect to the database 
connection = psycopg2.connect(host='localhost', port='5432', database='comment_classification', user='evermal', password= '')
cursor = connection.cursor()

cursor.execute("select commenttext, id from processed_comment")
processed_comment_list = cursor.fetchall()

formatted_comment_list = []
formatted_comment_id_list = []

for processed_comment in processed_comment_list:
    formatted_comment = " ".join(processed_comment[0].lower().replace('\n','').replace('\r\n', '').replace('\r', '').replace('\t', '').replace('//','').replace('/**','').replace('*/','').replace('/*','').replace('*','').replace(',','').replace(':','').replace('...','').replace(';','').split())
    formatted_comment_list.append(formatted_comment)
    formatted_comment_id_list.append(processed_comment[1])

print 'inserting data ...'
progress_counter = 0
total_comments = len(formatted_comment_id_list)
for x in xrange(0, total_comments):
    progress_counter = progress_counter + 1
    cursor.execute("update processed_comment set treated_commenttext = %s where id = %s", (formatted_comment_list[x], formatted_comment_id_list[x]))
    connection.commit()
    print str(progress_counter) + ' out of : ' + str(total_comments)
print 'done'
