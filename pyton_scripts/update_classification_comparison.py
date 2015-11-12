#!/usr/bin/python

import psycopg2
import sys
import os
import re
import time
import shutil
import codecs
import subprocess
import pexpect
import sys
from xlwings import Workbook, Sheet, Range, Chart

password = sys.argv[1]

connection = None
# connect to the database 
connection = psycopg2.connect(host='localhost', port='5432', database='comment_classification', user='evermal', password= password)
cursor = connection.cursor()

final_workbook = Workbook('/Users/evermal/Downloads/technical_debt_review.xls')

# go through each line of the table
for x in xrange(2,249):
    # set the profesors spreedsheet as current workbook
    final_workbook.set_current()
    comment_id_cell = str(Range('A'+str(x)).value).replace('.0', '')
    if comment_id_cell is not None:
        final_classification_cell = Range('E'+str(x)).value

    # print comment_id_cell
    # print final_classification_cell

    # print "update significative_sample set reviewerclassification = '"+final_classification_cell+"' where reviewer= 'Sultan' and processedcommentid ="+comment_id_cell
    cursor.execute("update significative_sample set reviewerclassification = '"+final_classification_cell+"' where reviewer= 'Sultan' and processedcommentid ="+str(comment_id_cell))
    connection.commit()