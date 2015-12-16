# figure 2 
# size 29 x 15
# generate figure to compare f1measure, baseline f1measure and rdn F1 measure for all projects (design debt)
mydata <- data.frame(Ant= c(0.517, 0.175,  0.045),ArgoUML= c(0.814, 0.078,  0.155),Columba= c(0.601, 0.145,  0.038),EMF= c(0.470, 0.114,  0.035),Hibernate= c(0.744,  0.15,  0.214),JEdit= c(0.509, 0.324,  0.037),JFreeChart= c(0.492, 0.053,   0.08),Jmeter= c(0.731, 0.127,  0.075),JRuby= c(0.783, 0.138,  0.131),SQuirrel= c(0.540, 0.071,  0.056))
barplot(as.matrix(mydata),  ylim=c(0, 1), ylab="",xlab="", beside=TRUE, col= terrain.colors(3), cex.axis=2.3, cex.names=2.3, mgp = c(3,2,1) )
legend(27, 1, c("Our approach", "Comment patterns", "Random classifier"), bty = "n" , cex=2.3, fill=terrain.colors(3))
title(ylab = "F1 Measure", mgp = c(3, 0, 0), cex.lab=2.3)

# title(xlab = "Projects",   mgp = c(4.5, 1, 0), cex.lab=2.3)

# figure 2 
# size 29 x 15
# generate figure to compare f1measure, baseline f1measure and rdn F1 measure for all projects (requirement debt)
mydata <- data.frame(Ant= c(0.154, 0.0, 0.006 ),ArgoUML= c(0.595, 0.0, 0.083 ),Columba= c(0.804, 0.0, 0.013 ),EMF= c(0.381, 0.0, 0.007 ),Hibernate= c(0.476, 0.0, 0.042 ),JEdit= c(0.091, 0.0, 0.003 ),JFreeChart= c(0.321, 0.0, 0.007 ),Jmeter= c(0.237, 0.0, 0.005 ),JRuby= c(0.435, 0.0, 0.044 ),SQuirrel= c(0.541, 0.0, 0.014 ))
barplot(as.matrix(mydata),  ylim=c(0, 1), ylab="",xlab="", beside=TRUE, col= terrain.colors(3), cex.axis=2.3, cex.names=2.3, mgp = c(3,2,1) )
legend(27, 1, c("Our approach", "Comment patterns", "Random classifier"), bty = "n" , cex=2.3, fill=terrain.colors(3))
title(ylab = "F1 Measure", mgp = c(3, 0, 0), cex.lab=2.3)


# figure 3 and 4 
# size 10 x 7.5
# generate comparison between td classified and random measured
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1, baselinef1 from classifier_results where projectname like '%ant%' and category = 'DESIGN' and classificationid=7  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1, baselinef1 from classifier_results where projectname like '%jmeter%' and category = 'DESIGN' and classificationid=7  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1, baselinef1 from classifier_results where projectname like '%argo%' and category = 'DESIGN' and classificationid=7  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1, baselinef1 from classifier_results where projectname like '%columba%' and category = 'DESIGN' and classificationid=7  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1, baselinef1 from classifier_results where projectname like '%emf%' and category = 'DESIGN' and classificationid=7  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1, baselinef1 from classifier_results where projectname like '%hibernate%' and category = 'DESIGN' and classificationid=7  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1, baselinef1 from classifier_results where projectname like '%jEdit%' and category = 'DESIGN' and classificationid=7  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1, baselinef1 from classifier_results where projectname like '%jfreechart%' and category = 'DESIGN' and classificationid=7  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1, baselinef1 from classifier_results where projectname like '%jruby%' and category = 'DESIGN' and classificationid=7  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1, baselinef1 from classifier_results where projectname like '%sql12%' and category = 'DESIGN' and classificationid=7  order by 1,2")

postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1, baselinef1 from classifier_results where projectname like '%ant%' and category = 'IMPLEMENTATION' and classificationid=7  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1, baselinef1 from classifier_results where projectname like '%jmeter%' and category = 'IMPLEMENTATION' and classificationid=7  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1, baselinef1 from classifier_results where projectname like '%argo%' and category = 'IMPLEMENTATION' and classificationid=7  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1, baselinef1 from classifier_results where projectname like '%columba%' and category = 'IMPLEMENTATION' and classificationid=7  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1, baselinef1 from classifier_results where projectname like '%emf%' and category = 'IMPLEMENTATION' and classificationid=7  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1, baselinef1 from classifier_results where projectname like '%hibernate%' and category = 'IMPLEMENTATION' and classificationid=7  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1, baselinef1 from classifier_results where projectname like '%jEdit%' and category = 'IMPLEMENTATION' and classificationid=7  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1, baselinef1 from classifier_results where projectname like '%jfreechart%' and category = 'IMPLEMENTATION' and classificationid=7  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1, baselinef1 from classifier_results where projectname like '%jruby%' and category = 'IMPLEMENTATION' and classificationid=7  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1, baselinef1 from classifier_results where projectname like '%sql12%' and category = 'IMPLEMENTATION' and classificationid=7  order by 1,2")

library(RPostgreSQL)
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, host='localhost', port='5432', dbname='comment_classification', user='evermal', password='')
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1, baselinef1 from classifier_results where projectname like '%ant%' and category = 'DESIGN' and classificationid=7  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1, baselinef1 from classifier_results where projectname like '%argo%' and category = 'IMPLEMENTATION' and classificationid=7  order by 1,2")

data1 <- fetch(postgresql, n=-1)
dim(data1)
dbHasCompleted(postgresql)
plot(data1$projectstrainedwith, data1$classifiedf1, type="b",
     col="red", lty=0, pch=2, lwd=2,
     xlab="Projects used in training dataset", ylab="F1 measure",
     xlim=c(0, 10), ylim=c(0, 1))
lines(data1$projectstrainedwith, data1$classifiedrandomf1, type="b", pch=22, col="blue", lty=0)
lines(data1$projectstrainedwith, data1$baselinef1, type="b", pch=21, col="darkgreen", lty=0)
abline(h=(data1$classifiedf1[which.max(data1$classifiedf1)] * .9), col="black", lty=2)
text(0.1, y=(data1$classifiedf1[which.max(data1$classifiedf1)] * .9 + 0.02), "90%", col = "black") 
abline(h=(data1$classifiedf1[which.max(data1$classifiedf1)] * .8), col="black", lty=2)
text(0.1, y=(data1$classifiedf1[which.max(data1$classifiedf1)] * .8 + 0.02), "80%", col = "black") 
legend(6, 1, c("Our approach", "Comment patterns", "Random classifier" ), col= c("red", "darkgreen",  "blue"), pch = c(2, 21, 22), bty = "n" , cex=1.1)


# figure 5 
# size 29 x 15
# generate figure to compare f1measure of different classification algorithms for design debt
mydata <- data.frame(Ant= c(0.517 , 0.563 , 0.134 ),ArgoUML= c(0.814 , 0.822 , 0.525 ),Columba= c(0.601 , 0.627 , 0.294 ),EMF= c(0.470 , 0.488 , 0.106 ),Hibernate= c(0.744 , 0.767 , 0.435 ),JEdit= c(0.509 , 0.480 , 0.353 ),JFreeChart= c(0.492 , 0.495 , 0.224 ),Jmeter= c(0.731 , 0.737 , 0.350 ),JRuby= c(0.783 , 0.811 , 0.429 ),SQuirrel= c(0.540 , 0.558 , 0.233 ))
barplot(as.matrix(mydata),  ylim=c(0, 1), ylab="",xlab="", beside=TRUE, col= terrain.colors(3), cex.axis=1, cex.names=2.3, mgp = c(0, 0.8, 0.5) )
legend(24, 1, c("Our approach", "Comment patterns", "Random classifier"), bty = "n" , cex=2.3, fill=terrain.colors(3))
title(ylab = "F1 Measure", mgp = c(2.2, 0, 0), cex.lab=2.0)

# barplot(as.matrix(mydata),  ylim=c(0, 1), beside=TRUE, col= terrain.colors(3), cex.lab=2,  cex.axis=2.3, cex.names=2.3, mgp = c(3, 2, 1) )
# legend("topright", c("Logistic Regression F1 measure",  "Binary F1 measure", "Naive Bayes F1 measure"), bty = "n" , cex=2.3, fill=terrain.colors(3))



# figure 5 
# size 29 x 15
# generate figure to compare f1measure of different classification algorithms for requirement debt
mydata <- data.frame(Ant= c(0.154, 0.207 , 0.057),ArgoUML= c(0.595, 0.611 , 0.022),Columba= c(0.804, 0.804 , 0.207),EMF= c(0.381, 0.381 , 0.018),Hibernate= c(0.476, 0.466 , 0.078),JEdit= c(0.091, 0.095 , 0.022),JFreeChart= c(0.321, 0.259 , 0.018),Jmeter= c(0.237, 0.268 , 0.013),JRuby= c(0.435, 0.442 , 0.109),SQuirrel= c(0.541, 0.476 , 0.036))
barplot(as.matrix(mydata),  ylim=c(0, 1), ylab="",xlab="", beside=TRUE, col= terrain.colors(3), cex.axis=1, cex.names=2.3, mgp = c(0, 0.8, 0.5) )
legend(24, 1, c("Our approach", "Comment patterns", "Random classifier"), bty = "n" , cex=2.3, fill=terrain.colors(3))
title(ylab = "F1 Measure", mgp = c(2.2, 0, 0), cex.lab=2.0)

# Textual similarity between requirement and design comments IMPLEMENTATION = 0.0389864024682, DESIGN = 0.0290795195597
  library(RPostgreSQL)
  library(vioplot)
  drv <- dbDriver("PostgreSQL")
  con <- dbConnect(drv, host='localhost', port='5432', dbname='comment_classification', user='evermal', password='')
  
  postgresql <- dbSendQuery(con, "select textual_similarity from processed_comment where classification = 'DESIGN'")
  design_similarity_results <- fetch(postgresql, n=-1)
  dim(design_similarity_results)
  
  postgresql <- dbSendQuery(con, "select textual_similarity from processed_comment where classification = 'IMPLEMENTATION'")
  implementation_similarity_results <- fetch(postgresql, n=-1)
  dim(implementation_similarity_results)
  
  dbHasCompleted(postgresql)
  
  vioplot(design_similarity_results$textual_similarity, implementation_similarity_results$textual_similarity, names=c("Design", "Requirement"),   col="gold")
  # title("Textual Similarity Between Design and Requiremt Debt Comments", ylab="Cosine Similarity")
  title(ylab="Cosine Similarity")

wilcox.test(design_similarity_results$textual_similarity, implementation_similarity_results$textual_similarity)
summary(design_similarity_results)
summary(implementation_similarity_results)

# average size of comments
library(RPostgreSQL)
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, host='localhost', port='5432', dbname='comment_classification', user='evermal', password='')
postgresql <- dbSendQuery(con, "select a.treated_commenttext from processed_comment a, comment_class b  where a.commentclassid = b.id and classification = 'IMPLEMENTATION' and projectname='jEdit-4.2'")
treated_commenttext_list <- fetch(postgresql, n=-1)
dim(treated_commenttext_list)
dbHasCompleted(postgresql)

treated_commenttext_list$treated_commenttext

barplot(nchar(treated_commenttext_list$treated_commenttext), main="Box plot", ylab="Miles per Gallon")

max(nchar(treated_commenttext_list$treated_commenttext))
mean(nchar(treated_commenttext_list$treated_commenttext))
# __________________________________________________________________________________________________________________________________________________________________________________________________________________________


# Appendix 
# generate figure to compare precision, recall and f1measure of all projects
mydata <- data.frame(Ant= c(0.597,0.389,0.471,0.55 ,0.082,0.142),Jmeter= c(0.848,0.601,0.704,0.733,0.058,0.108),ArgoUML= c(0.769,0.875,0.819,0.790,0.020,0.040),Columba= c(0.862,0.444,0.586,0.833,0.033,0.065),EMF= c(0.521,0.321,0.397,0.5  ,0.048,0.087),Hibernate= c(0.882,0.569,0.692,0.909,0.063,0.118),JEdit= c( 0.84,0.321,0.465,0.869,0.156,0.264),JFreeChart= c(0.689,0.397,0.503,0.833,0.022,0.044),JRuby= c(0.824,0.767,0.795,0.764,0.041,0.078),SQuirrel= c(0.598,0.498,0.543,0.5  ,0.023,0.044))
barplot(as.matrix(mydata),  ylab="Percentage",  ylim=c(0, 1), beside=TRUE, col= terrain.colors(6))
legend("topright", c("Precision", "Recall", "F1","Baseline P", "Baseline R", "Baseline F1"), cex=0.8, fill=terrain.colors(6))

# impact of the changes in the training dataset detailed design
mydata <- data.frame(Ant= c(0.511,0.471,0.517), Jmeter= c(0.744,0.704,0.731), ArgoUML= c(0.801,0.819,0.814), Columba= c(0.815,0.586,0.601), EMF= c(0.532,0.397,0.470), Hibernate= c(0.742,0.692,0.744), JEdit= c(0.493,0.465,0.509), JFreeChart= c(0.452,0.503,0.492), JRuby= c(0.817,0.795,0.783), SQuirrel= c(0.587,0.543,0.540))
barplot(as.matrix(mydata),  ylab="Percentage",  ylim=c(0, 1), beside=TRUE, col= terrain.colors(3))
legend("topright", c("Anagrams", "CapitalLetters", "Lowercase"), cex=0.8, fill=terrain.colors(3))

# impact of the changes in the training dataset average design
mydata <- data.frame(Anagrams= c(0.6494) , CapitalLetters= c(0.5975), Lowercase= c(0.6201))
barplot(as.matrix(mydata),  ylab="Percentage",  ylim=c(0, 1), beside=TRUE, col= terrain.colors(3))
# legend("topright", c("Ana", "Recall", "F1","Baseline P", "Baseline R", "Baseline F1"), cex=0.8, fill=terrain.colors(6))

# impact of the changes in the training dataset detailed requirements
mydata <- data.frame(Ant= c(0.581,0.462,0.987),Jmeter= c(0.531,0.393,0.255),ArgoUML= c(0.826,0.741,0.760),Columba= c(0.912,0.935,0.934),EMF= c(0.222,0.118,0.381),Hibernate= c(0.686,0.650,0.476),JEdit= c(0.133,0.100,0.091),JFreeChart= c(0.708,0.513,0.500),JRuby= c(0.626,0.463,0.462),SQuirrel= c(0.845,0.853,0.875))
barplot(as.matrix(mydata),  ylab="Percentage",  ylim=c(0, 1), beside=TRUE, col= terrain.colors(3))
legend("topright", c("Anagrams", "CapitalLetters", "Lowercase"), cex=0.8, fill=terrain.colors(3))

# impact of the changes in the training dataset average requirements
mydata <- data.frame(Anagrams= c(0.607) , CapitalLetters= c(0.5228), Lowercase= c(0.5721))
barplot(as.matrix(mydata),  ylab="Percentage",  ylim=c(0, 1), beside=TRUE, col= terrain.colors(3))
# legend("topright", c("Ana", "Recall", "F1","Baseline P", "Baseline R", "Baseline F1"), cex=0.8, fill=terrain.colors(6))

# Cohen's kappa FOR THE DATASET
library(RPostgreSQL)
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, host='localhost', port='5432', dbname='comment_classification', user='evermal', password='')
postgresql <- dbSendQuery(con, "select classification from significative_sample order by processedcommentid")
reviewer1 <- fetch(postgresql, n=-1)
dim(reviewer1)
dbHasCompleted(postgresql)

library(RPostgreSQL)
library(psych)
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, host='localhost', port='5432', dbname='comment_classification', user='evermal', password='')
postgresql <- dbSendQuery(con, "select reviewerclassification from significative_sample order by processedcommentid")
reviewer2 <- fetch(postgresql, n=-1)
dim(reviewer2)
dbHasCompleted(postgresql)
xy.df <- data.frame(reviewer1,reviewer2)
ck <- cohen.kappa(xy.df)
ck
ck$agree

# __________________________________________________________________________________________________________________________________________________________________________________________________________________________