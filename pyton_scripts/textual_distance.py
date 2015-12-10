#!/usr/bin/python

import psycopg2
from sklearn.feature_extraction.text import TfidfVectorizer

# connect to the database 
connection = psycopg2.connect(host='localhost', port='5432', database='comment_classification', user='evermal', password= '')
cursor = connection.cursor()

cursor.execute("select commenttext, id from processed_comment where classification = 'IMPLEMENTATION' order by 2")
processed_comment_list = cursor.fetchall()

formatted_comment_list = []
formatted_comment_id_list = []

for processed_comment in processed_comment_list:
    formatted_comment = " ".join(processed_comment[0].lower().replace('\n','').replace('\r\n', '').replace('\r', '').replace('\t', '').replace('//','').replace('/**','').replace('*/','').replace('/*','').replace('*','').replace(',','').replace(':','').replace('...','').replace(';','').split())
    formatted_comment_list.append(formatted_comment)
    formatted_comment_id_list.append(processed_comment[1])

vect = TfidfVectorizer(min_df=1)
tfidf = vect.fit_transform(formatted_comment_list)

# .A transforms a sparse matrix to a dense one, for the purpose of printing it. .T means transpose
pairwise_similarity_lists = (tfidf * tfidf.T).A

pairwise_similarity_means = pairwise_similarity_lists.mean(1)
print pairwise_similarity_means

print len(formatted_comment_id_list)
print len(pairwise_similarity_means)

print pairwise_similarity_lists.mean()

# print 'inserting data ...'
# for x in xrange(0, len(formatted_comment_id_list)):
#     cursor.execute("update processed_comment set textual_similarity = %s where id = %s", (pairwise_similarity_means[x], formatted_comment_id_list[x]))
# print 'done'
# connection.commit()