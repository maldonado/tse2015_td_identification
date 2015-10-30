-- Number of TD per file
select a.filename, count(*) from comment_class a, processed_comment b where a.id = b.commentclassid and b.classification not in ('WITHOUT_CLASSIFICATION', 'BUG_FIX_COMMENT') and a.projectname like '%ant%' group by 1 order by 1;

-- Number of TD per file (files with more than one TD only)
select a.filename, count(*) from comment_class a, processed_comment b where a.id = b.commentclassid and b.classification not in ('WITHOUT_CLASSIFICATION', 'BUG_FIX_COMMENT') and a.projectname like '%ant%' group by 1 having count(*) > 1 order by 1;

-- Number of different TD types per file
select a.filename, b.classification, count(*) from comment_class a, processed_comment b where a.id = b.commentclassid and b.classification not in ('WITHOUT_CLASSIFICATION', 'BUG_FIX_COMMENT') and a.projectname like '%ant%' group by 1,2  order by 1;

 
 CBZip2OutputStream.java     | DESIGN         |     1
 CBZip2OutputStream.java     | IMPLEMENTATION |     1
 
 Classloader.java            | DESIGN         |     1
 Classloader.java            | IMPLEMENTATION |     2
  
 FTP.java                    | DESIGN         |     1
 FTP.java                    | IMPLEMENTATION |     1
 
 GenericDeploymentTool.java  | DESIGN         |     1
 GenericDeploymentTool.java  | IMPLEMENTATION |     1
 
 JDependTask.java            | DESIGN         |     4
 JDependTask.java            | TEST           |     1
 
 Jar.java                    | DESIGN         |     1
 Jar.java                    | IMPLEMENTATION |     1
 
 JikesOutputParser.java      | DEFECT         |     1
 JikesOutputParser.java      | DESIGN         |     2
 
 
 ModifiedSelector.java       | DESIGN         |     1
 ModifiedSelector.java       | IMPLEMENTATION |     1
 

 PropertyHelper.java         | DESIGN         |     3
 PropertyHelper.java         | IMPLEMENTATION |     1
 
 StyleTest.java              | DESIGN         |     1
 StyleTest.java              | TEST           |     1
 
 TraXLiaison.java            | DEFECT         |     2
 TraXLiaison.java            | DESIGN         |     2
 
 
 XmlPropertyTest.java        | DESIGN         |     1
 XmlPropertyTest.java        | TEST           |     1
 

