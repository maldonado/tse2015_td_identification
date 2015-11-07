-- auxiliar scripts to drop tables
drop table comment_class;
drop table comment;
drop table processed_comment;

#1 create table in postgresql
drop table if exists comment_class;
create table comment_class (
    id serial primary key,
    projectName text,
    fileName text,
    className text,
    access text,
    isAbstract text,
    isEnum text,
    isInterface text, 
    startline integer,
    endline integer, 
    analyzed integer
); 

drop table if exists comment;
CREATE TABLE comment (
    commentClassId integer,
    startLine integer, 
    endLine integer,
    commentText text,
    commentType text,
    location text,
    description text , 
    dictionary_hit text, 
    jdeodorant_hit text, 
    refactoring_list_name text
);

drop table if exists processed_comment;
CREATE TABLE processed_comment (
    commentClassId integer,
    startLine integer, 
    endLine integer,
    commentText text,
    commentType text,
    location text,
    description text, 
    dictionary_hit text, 
    jdeodorant_hit text, 
    refactoring_list_name text
);
pg_dump -Fc -Uevermal comment_classification > ~/Dropbox/research/database_backups/comment_classification/comment_classification_backup.dump
#1 create table in postgresql
drop table if exists classifier_results;
create table classifier_results (
projectName text,
classificationid integer,
classificationDescription text,
category text,
projectsTrainedWith integer,
totalTrainingComments integer,
withoutClassificationCommentsTrain integer,
classifiedCommentsTrain integer,
totalTestComments integer,
withoutClassificationCommentsTest integer,
classifiedCommentsTest integer,
classifiedTP integer, 
classifiedFN integer,
classifiedFP integer,
classifiedTN integer, 
classifiedAccuracy numeric,
classifiedPrecision numeric,
classifiedRecall numeric,
classifiedF1 numeric,
classifiedRandomPrecision numeric,
classifiedRandomRecall numeric,
classifiedRandomF1 numeric,
withoutClassificationTP integer, 
withoutClassificationFN integer,
withoutClassificationFP integer,
withoutClassificationTN integer, 
withoutClassificationAccuracy numeric,
withoutClassificationPrecision numeric,
withoutClassificationRecall numeric,
withoutClassificationF1 numeric,
withoutClassificatioRandomPrecision numeric,
withoutClassificatioRandomRecall numeric,
withoutClassificatioRandomF1 numeric,
microAveragedF1 numeric,
macroAveragedF1 numeric, 
baselinePrecision numeric,
baselineRecall numeric,
baselineF1 numeric
); 

drop table if exists significative_sample;
create table significative_sample (
    processedCommentId integer,
    projectName text,
    commentText text,
    classification text,
    reviewer text,
    reviewerClassification text
);

drop table if exists performance_per_iteration;
create table performance_per_iteration (
    classificationid text,
    category text, 
    projectname text,
    projectstrainedwith numeric,
    totalTrainingComments numeric, 
    classifiedF1 numeric,
    percentage_of_maximum_performance numeric 
);

insert into significative_sample (processedCommentId,commentText,classification) 
  select id, commentText, classification 
    from processed_comment where classification = 'WITHOUT_CLASSIFICATION' limit 609

insert into significative_sample (processedCommentId,commentText,classification) 
  select id, commentText, classification 
    from processed_comment where classification = 'DESIGN' limit 29

insert into significative_sample (processedCommentId,commentText,classification) 
  select id, commentText, classification 
    from processed_comment where classification = 'IMPLEMENTATION' limit 13

insert into significative_sample (processedCommentId,commentText,classification) 
  select id, commentText, classification 
    from processed_comment where classification = 'DEFECT' limit 5    

insert into significative_sample (processedCommentId,commentText,classification) 
  select id, commentText, classification 
    from processed_comment where classification = 'TEST' limit 2    

insert into significative_sample (processedCommentId,commentText,classification) 
  select id, commentText, classification 
    from processed_comment where classification = 'DOCUMENTATION' limit 1  

with temporary as (
  
  select b.projectname, a.id as processedCommentId from processed_comment a, comment_class b where a.commentClassId = b.id 
    
  )
update significative_sample set projectname = r.projectname from temporary r where r.processedCommentId = significative_sample.processedCommentId;      




#2 run eclipse.commandline application adapted to run with postgresql to parse the comments and collect the raw comments.
-- alternatively , is possible to run sqlite_to_postgresql.py for each sqlite database file. i did not do that because 
-- the sqlite files as not reliable and there was multiple versions of them.

-- check both databases
select count(*) from comment_class where projectName = 'apache-ant-1.7.0';
select count(*) from comment_class where projectName = 'apache-jmeter-2.10';
select count(*) from comment_class where projectName like 'argouml%';
select count(*) from comment_class where projectName = 'columba-1.4-src';
select count(*) from comment_class where projectName = 'emf-2.4.1';
select count(*) from comment_class where projectName = 'hibernate-distribution-3.3.2.GA';
select count(*) from comment_class where projectName = 'jEdit-4.2';
select count(*) from comment_class where projectName = 'jfreechart-1.0.19';
select count(*) from comment_class where projectName = 'jruby-1.4.0';
select count(*) from comment_class where projectName = 'sql12';
-- in postgresql vs lite number of classes
  1475 1475 ok                
  1181 1181 ok            
  2610 2609 nok argo (need to be corrected , evernote created)       
  1711 1711 ok            
  1458 1458 ok            
  1356 1356 ok
   800 800  ok            
  1065 1065 ok
  1486 1486 ok            
  3108 3108 ok
select count(*) from comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'apache-ant-1.7.0';
select count(*) from comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'apache-jmeter-2.10';
select count(*) from comment a, comment_class b where a.commentclassid = b.id  and b.projectname like 'argouml%';
select count(*) from comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'columba-1.4-src';
select count(*) from comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'emf-2.4.1';
select count(*) from comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'hibernate-distribution-3.3.2.GA';
select count(*) from comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'jEdit-4.2';
select count(*) from comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'jfreechart-1.0.19';
select count(*) from comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'jruby-1.4.0';
select count(*) from comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'sql12';
-- in postgresql vs lite number of comments
 21587 21587 ok
 20084 20084 ok
 67719 67716 nok argo  (need to be corrected , evernote created)       
 33895 33895 ok
 25229 25229 ok
 11630 11630 ok
 16991 16991 ok
 23123 23123 ok
 11149 11149 ok
 27474 27474 ok

#3 dump the database in the raw state. keep this state of the database (available in dropbox)

#4 create index as necessary 
CREATE INDEX idx_comment_comment_class_id ON comment (commentclassid);
CREATE INDEX idx_processed_comment_comment_class_id ON processed_comment (commentclassid);

#5 dump database with the created indexes

#6 run filters using eclipse.commandline application
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'apache-ant-1.7.0';
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'apache-jmeter-2.10';
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like 'argouml%';
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'columba-1.4-src';
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'emf-2.4.1';
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'hibernate-distribution-3.3.2.GA';
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'jEdit-4.2';
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'jfreechart-1.0.19';
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'jruby-1.4.0';
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'sql12';
-- in postgresql vs lite number of comments
--(third column is final after the correction of the inner class)
'apache-ant-1.7.0';                4417  4436    4140
'apache-jmeter-2.10';              7973  8126    8163
'argouml%';                        10189 10303   9788 
'columba-1.4-src';                 6675  6825    6569
'emf-2.4.1';                        5085 5868    4401
'hibernate-distribution-3.3.2.GA';  3032 3071    2968
'jEdit-4.2';                       11205 11232  10322 
'jfreechart-1.0.19';                4412 4449    4433
'jruby-1.4.0';                      5081 5176    4901
'sql12';                            8519 8627    7330



(the difference is normal because of the order of the filters that changed , see evernote log for more information)

#7 dump database with filtered comments

#8 insert classification columns into processed_comments
ALTER TABLE comment add column classification text;
ALTER TABLE processed_comment add column classification text;

#insert already classified comments into the database (ant, jmeter, freechart)

#9 Run web applicarition to classify all comments

-- get numbers 
-- everything that was classified
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'apache-ant-1.7.0';
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like 'argouml%';
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'columba-1.4-src';
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'emf-2.4.1';
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'hibernate-distribution-3.3.2.GA';
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'jEdit-4.2';
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'jfreechart-1.0.19';
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'apache-jmeter-2.10';
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'jruby-1.4.0';
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like 'sql12%';

-- everything that was classified as without classification (bug fix comments are not a category of technical debt is that why it is here)
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'apache-ant-1.7.0' and a.classification in ('WITHOUT_CLASSIFICATION', 'BUG_FIX_COMMENT');
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like 'argouml%' and a.classification in ('WITHOUT_CLASSIFICATION', 'BUG_FIX_COMMENT');
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'columba-1.4-src' and a.classification in ('WITHOUT_CLASSIFICATION', 'BUG_FIX_COMMENT');
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'emf-2.4.1' and a.classification in ('WITHOUT_CLASSIFICATION' ,'BUG_FIX_COMMENT');
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'hibernate-distribution-3.3.2.GA' and a.classification in ('WITHOUT_CLASSIFICATION' ,'BUG_FIX_COMMENT');
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'jEdit-4.2' and a.classification in ('WITHOUT_CLASSIFICATION', 'BUG_FIX_COMMENT');
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'jfreechart-1.0.19' and a.classification in ('WITHOUT_CLASSIFICATION', 'BUG_FIX_COMMENT');
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'apache-jmeter-2.10' and a.classification in ('WITHOUT_CLASSIFICATION' ,'BUG_FIX_COMMENT');
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'jruby-1.4.0' and a.classification in ('WITHOUT_CLASSIFICATION', 'BUG_FIX_COMMENT');
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like 'sql12%' and a.classification in ('WITHOUT_CLASSIFICATION', 'BUG_FIX_COMMENT');

-- everything that was clasified as technical debt
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'apache-ant-1.7.0' and a.classification not in ('WITHOUT_CLASSIFICATION' ,'BUG_FIX_COMMENT');
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like 'argouml%' and a.classification not in ('WITHOUT_CLASSIFICATION', 'BUG_FIX_COMMENT');
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'columba-1.4-src' and a.classification not in ('WITHOUT_CLASSIFICATION', 'BUG_FIX_COMMENT');
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'emf-2.4.1' and a.classification not in ('WITHOUT_CLASSIFICATION' ,'BUG_FIX_COMMENT');
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'hibernate-distribution-3.3.2.GA' and a.classification not in ('WITHOUT_CLASSIFICATION' ,'BUG_FIX_COMMENT');
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'jEdit-4.2' and a.classification not in ('WITHOUT_CLASSIFICATION', 'BUG_FIX_COMMENT');
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'jfreechart-1.0.19' and a.classification not in ('WITHOUT_CLASSIFICATION', 'BUG_FIX_COMMENT');
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'apache-jmeter-2.10' and a.classification not in ('WITHOUT_CLASSIFICATION' ,'BUG_FIX_COMMENT');
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'jruby-1.4.0' and a.classification not in ('WITHOUT_CLASSIFICATION', 'BUG_FIX_COMMENT');
select count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like 'sql12%' and a.classification not in ('WITHOUT_CLASSIFICATION', 'BUG_FIX_COMMENT');



-- techinical debt distribution per project
select a.classification, count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'apache-ant-1.7.0' and a.classification not in ('BUG_FIX_COMMENT') group by 1;
 WITHOUT_CLASSIFICATION |  3967
 DESIGN                 |    95
 TEST                   |    10
 IMPLEMENTATION         |    13
 DEFECT                 |    13
select a.classification, count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname like 'argouml%' and a.classification not in ('BUG_FIX_COMMENT') group by 1;
 WITHOUT_CLASSIFICATION |  8039
 DESIGN                 |   801
 DOCUMENTATION          |    30
 TEST                   |    44
 IMPLEMENTATION         |   411
 DEFECT                 |   127
select a.classification, count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'columba-1.4-src' and a.classification not in ('BUG_FIX_COMMENT') group by 1;
 WITHOUT_CLASSIFICATION |  6264
 DESIGN                 |   126
 DOCUMENTATION          |    16
 IMPLEMENTATION         |    43
 TEST                   |     6
 DEFECT                 |    13
select a.classification, count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'emf-2.4.1' and a.classification not in ('BUG_FIX_COMMENT') group by 1;
 WITHOUT_CLASSIFICATION |  4286
 DESIGN                 |    78
 IMPLEMENTATION         |    16
 TEST                   |     2
 DEFECT                 |     8
select a.classification, count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'hibernate-distribution-3.3.2.GA' and a.classification not in ('BUG_FIX_COMMENT') group by 1;
 WITHOUT_CLASSIFICATION |  2496
 DESIGN                 |   355
 DOCUMENTATION          |     1
 IMPLEMENTATION         |    64
 DEFECT                 |    52
select a.classification, count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'jEdit-4.2' and a.classification not in ('BUG_FIX_COMMENT') group by 1;
 WITHOUT_CLASSIFICATION | 10066
 DESIGN                 |   196
 IMPLEMENTATION         |    14
 TEST                   |     3
 DEFECT                 |    43
select a.classification, count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'jfreechart-1.0.19' and a.classification not in ('BUG_FIX_COMMENT') group by 1;
 WITHOUT_CLASSIFICATION |  4199
 DESIGN                 |   184
 IMPLEMENTATION         |    15
 TEST                   |     1
 DEFECT                 |     9
select a.classification, count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'apache-jmeter-2.10' and a.classification not in ('BUG_FIX_COMMENT') group by 1;
 WITHOUT_CLASSIFICATION |  7683
 DESIGN                 |   316
 DOCUMENTATION          |     3
 IMPLEMENTATION         |    21
 TEST                   |    12
 DEFECT                 |    22
select a.classification, count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'jruby-1.4.0' and a.classification not in ('BUG_FIX_COMMENT') group by 1;
 WITHOUT_CLASSIFICATION |  4275
 DESIGN                 |   343
 DOCUMENTATION          |     2
 IMPLEMENTATION         |   110
 TEST                   |     6
 DEFECT                 |   161
select a.classification, count(*) from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'sql12' and a.classification not in ('BUG_FIX_COMMENT') group by 1;
 WITHOUT_CLASSIFICATION |  6929
 DESIGN                 |   209
 DOCUMENTATION          |     2
 IMPLEMENTATION         |    50
 TEST                   |     1
 DEFECT                 |    24

-- techinical debt examples per project and type
select a.commenttext, a.classification from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'apache-ant-1.7.0'   and a.classification in ('DOCUMENTATION') order by 2;  
select a.commenttext, a.classification from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'apache-ant-1.7.0'   and a.classification in ('DESIGN') order by 2;         
select a.commenttext, a.classification from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'apache-ant-1.7.0'   and a.classification in ('DEFECT') order by 2;         
select a.commenttext, a.classification from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'apache-ant-1.7.0'   and a.classification in ('IMPLEMENTATION') order by 2; 
select a.commenttext, a.classification from processed_comment a, comment_class b where a.commentclassid = b.id  and b.projectname = 'apache-ant-1.7.0'   and a.classification in ('TEST') order by 2;           
select b.projectname, a.commenttext from processed_comment a, comment_class b where a.commentclassid = b.id  where b.commentText = "TODO: - This method is too complex, lets break it up" 
select b.projectname, a.commenttext from processed_comment a, comment_class b where a.commentclassid = b.id  and a.commenttext like '%TODO enable some proper tests!!%';


-- gettinh precision , recall , random and baselines .... 
select projectname, classifiedPrecision, classifiedRecall, classifiedF1, baselinePrecision, baselineRecall, baselineF1, classifiedRandomPrecision, classifiedRandomRecall, classifiedRandomF1 from classifier_results where projectsTrainedWith = 9 and category = 'DESIGN' and classificationid = '8'


-- getting  best iterations
select projectname, classifiedf1, projectstrainedwith from classifier_results  where classificationid = 3 and category = 'DESIGN'  order by 1,2 desc;


-- 
select projectname, classifiedPrecision, classifiedRecall, classifiedF1, baselinePrecision, baselineRecall, baselineF1, classifiedRandomPrecision, classifiedRandomRecall, classifiedRandomF1 from classifier_results where projectsTrainedWith = 9 and category = 'IMPLEMENTATION' and classificationid = '3';
