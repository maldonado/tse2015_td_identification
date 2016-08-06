# _________________________________________________________________________________________________________________________________________________________________
# Fig. 2. Visualization of the F1-measure for Different Approaches (a) Design Debt
# size 29 x 15
mydata <- data.frame(Ant=c(0.517,0.237,0.044),ArgoUML=c(0.814,0.107,0.144),Columba=c(0.601,0.264,0.037),EMF=c(0.470,0.231,0.034),Hibernate=c(0.744,0.227,0.193),JEdit=c(0.509,0.342,0.037),JFreeChart=c(0.492,0.282,0.077),JMeter=c(0.731,0.194,0.072),JRuby=c(0.783,0.620,0.123),SQuirrel=c(0.540,0.175,0.055))
barplot(as.matrix(mydata),  ylim=c(0, 1), ylab="",xlab="", beside=TRUE, col= terrain.colors(3), cex.axis=2.3, cex.names=2.3, mgp = c(3,1.8,1) )
legend(21, 1, c("NLP-based", "Comment patterns", "Random classifier"), bty = "n" , cex=2.3, fill=terrain.colors(3))
title(ylab = "F1-Measure", mgp = c(4.5, 0, 0), cex.lab=2.3)
par("mar"=c(5,4,4,1)+3) 

# Fig. 2. Visualization of the F1-measure for Different Approaches (b) Requirement Debt
# size 29 x 15
mydata <- data.frame(Ant=c(0.154,0.000,0.006),ArgoUML=c(0.595,0.000,0.079),Columba=c(0.804,0.117,0.013),EMF=c(0.381,0.000,0.007),Hibernate=c(0.476,0.000,0.041),JEdit=c(0.091,0.000,0.003),JFreeChart=c(0.321,0.000,0.007),JMeter=c(0.237,0.148,0.005),JRuby=c(0.435,0.409,0.043),SQuirrel=c(0.541,0.000,0.014))
barplot(as.matrix(mydata),  ylim=c(0, 1), ylab="",xlab="", beside=TRUE, col= terrain.colors(3), cex.axis=2.3, cex.names=2.3, mgp = c(3,1.8,1) )
legend(21, 1, c("NLP-based", "Comment patterns", "Random classifier"), bty = "n" , cex=2.3, fill=terrain.colors(3))
title(ylab = "F1-Measure", mgp = c(4.5, 0, 0), cex.lab=2.3)
par("mar"=c(5,4,4,1)+3) 
# _________________________________________________________________________________________________________________________________________________________________

# Fig. 3. F1-measure achieved by incrementally adding batches of 100 comments in the training dataset. (a) Design Debt and (b) Requirement Debt
# size 12 x 9.5

# id = 1 => dataset without correct ratio (ten fold)
# id = 2 => design dataset batches of 100 comments (ten fold)
# id = 3 => design dataset batches of 500 comments (ten fold)
# id = 4 => design dataset batches of 100 comments (average)
# id = 5 => design dataset batches of 500 comments (average)
# id = 6 => requirement dataset batches of 100 comments (ten fold)
# id = 7 => requirement dataset batches of 500 comments (ten fold)
# id = 8 => requirement dataset batches of 100 comments (average)
# id = 9 => requirement dataset batches of 500 comments (average)

library(RPostgreSQL)
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, host='localhost', port='5432', dbname='comment_classification', user='evermal', password='')
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1  from classifier_results_ten_fold where category = 'DESIGN' and classificationid=4  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1  from classifier_results_ten_fold where category = 'REQUIREMENT' and classificationid=8  order by 1,2")
data1 <- fetch(postgresql, n=-1)
dim(data1)
dbHasCompleted(postgresql)

plot(data1$projectstrainedwith, data1$classifiedf1, type="b",
     col="red", lty=0, pch=2, lwd=2,
     xlab="Comments used in training dataset", ylab="F1-Measure",
     xlim=c(0, 57000), ylim=c(0, 1))

# horizontal line to present the 90% of the maximum F1-Measure
abline(h=(data1$classifiedf1[which.max(data1$classifiedf1)] * .9), col="black", lty=2)
text(0.1, y=(data1$classifiedf1[which.max(data1$classifiedf1)] * .9 + 0.02), "90%", col = "black") 
# horizontal line to present the 80% of the maximum F1-Measure
abline(h=(data1$classifiedf1[which.max(data1$classifiedf1)] * .8), col="black", lty=2)
text(0.1, y=(data1$classifiedf1[which.max(data1$classifiedf1)] * .8 + 0.02), "80%", col = "black") 
# vertical line to present the number of comments used to achieve 90% of the maximum F1-Measure
abline(v=(data1$projectstrainedwith[min(which(data1$classifiedf1 > data1$classifiedf1[which.max(data1$classifiedf1)] * .9))]), col="black", lty=2)
text(-0.01, x=(data1$projectstrainedwith[min(which(data1$classifiedf1 > data1$classifiedf1[which.max(data1$classifiedf1)] * .9))]), data1$projectstrainedwith[min(which(data1$classifiedf1 > data1$classifiedf1[which.max(data1$classifiedf1)] * .9))], col = "black")
# vertical line to present the number of comments used to achieve 80% of the maximum F1-Measure
abline(v=(data1$projectstrainedwith[min(which(data1$classifiedf1 > data1$classifiedf1[which.max(data1$classifiedf1)] * .8))]), col="black", lty=2)
text(-0.01, x=(data1$projectstrainedwith[min(which(data1$classifiedf1 > data1$classifiedf1[which.max(data1$classifiedf1)] * .8))]), data1$projectstrainedwith[min(which(data1$classifiedf1 > data1$classifiedf1[which.max(data1$classifiedf1)] * .8))], col = "black")

#each plot from the 10 fold validadion 
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1  from classifier_results_ten_fold where projectname = '0' and category = 'DESIGN' and classificationid=  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1  from classifier_results_ten_fold where projectname = '1' and category = 'DESIGN' and classificationid=  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1  from classifier_results_ten_fold where projectname = '2' and category = 'DESIGN' and classificationid=  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1  from classifier_results_ten_fold where projectname = '3' and category = 'DESIGN' and classificationid=  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1  from classifier_results_ten_fold where projectname = '4' and category = 'DESIGN' and classificationid=  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1  from classifier_results_ten_fold where projectname = '5' and category = 'DESIGN' and classificationid=  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1  from classifier_results_ten_fold where projectname = '6' and category = 'DESIGN' and classificationid=  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1  from classifier_results_ten_fold where projectname = '7' and category = 'DESIGN' and classificationid=  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1  from classifier_results_ten_fold where projectname = '8' and category = 'DESIGN' and classificationid=  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1  from classifier_results_ten_fold where projectname = '9' and category = 'DESIGN' and classificationid=  order by 1,2")
# 
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1  from classifier_results_ten_fold where projectname = '0' and category = 'REQUIREMENT' and classificationid=  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1  from classifier_results_ten_fold where projectname = '1' and category = 'REQUIREMENT' and classificationid=  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1  from classifier_results_ten_fold where projectname = '2' and category = 'REQUIREMENT' and classificationid=  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1  from classifier_results_ten_fold where projectname = '3' and category = 'REQUIREMENT' and classificationid=  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1  from classifier_results_ten_fold where projectname = '4' and category = 'REQUIREMENT' and classificationid=  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1  from classifier_results_ten_fold where projectname = '5' and category = 'REQUIREMENT' and classificationid=  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1  from classifier_results_ten_fold where projectname = '6' and category = 'REQUIREMENT' and classificationid=  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1  from classifier_results_ten_fold where projectname = '7' and category = 'REQUIREMENT' and classificationid=  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1  from classifier_results_ten_fold where projectname = '8' and category = 'REQUIREMENT' and classificationid=  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1  from classifier_results_ten_fold where projectname = '9' and category = 'REQUIREMENT' and classificationid=  order by 1,2")
# _________________________________________________________________________________________________________________________________________________________________

# Fig. 4. Textual Similarity Between Design and Requirement Debt Comments
# size 12 x 9.5
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
title(ylab="Cosine Similarity")

# wilcox test
wilcox.test(design_similarity_results$textual_similarity, implementation_similarity_results$textual_similarity)
summary(design_similarity_results)
summary(implementation_similarity_results)


# _________________________________________________________________________________________________________________________________________________________________


# Fig. 5. Underlying Classifier Algorithms Performance Comparison (a) Design Debt
# size 29 x 15
mydata <- data.frame(Ant= c(0.517 , 0.563 , 0.134 ),ArgoUML= c(0.814 , 0.822 , 0.525 ),Columba= c(0.601 , 0.627 , 0.294 ),EMF= c(0.470 , 0.488 , 0.106 ),Hibernate= c(0.744 , 0.767 , 0.435 ),JEdit= c(0.509 , 0.480 , 0.353 ),JFreeChart= c(0.492 , 0.495 , 0.224 ),JMeter= c(0.731 , 0.737 , 0.350 ),JRuby= c(0.783 , 0.811 , 0.429 ),SQuirrel= c(0.540 , 0.558 , 0.233 ))
barplot(as.matrix(mydata),  ylim=c(0, 1), ylab="",xlab="", beside=TRUE, col= terrain.colors(3), cex.axis=2.3, cex.names=2.3, mgp = c(3,1.8,1) )
legend(21, 1, c("Logistic Regression",  "Binary", "Naive Bayes"), bty = "n" , cex=2.3, fill=terrain.colors(3))
title(ylab = "F1-Measure", mgp = c(4.5, 0, 0), cex.lab=2.3)
par("mar"=c(5,4,4,1)+3) 

# Fig. 5. Underlying Classifier Algorithms Performance Comparison (a) Requirement Debt
# size 29 x 15
mydata <- data.frame(Ant= c(0.154, 0.207 , 0.057),ArgoUML= c(0.595, 0.611 , 0.022),Columba= c(0.804, 0.804 , 0.207),EMF= c(0.381, 0.381 , 0.018),Hibernate= c(0.476, 0.466 , 0.078),JEdit= c(0.091, 0.095 , 0.022),JFreeChart= c(0.321, 0.259 , 0.018),JMeter= c(0.237, 0.268 , 0.013),JRuby= c(0.435, 0.442 , 0.109),SQuirrel= c(0.541, 0.476 , 0.036))
barplot(as.matrix(mydata),  ylim=c(0, 1), ylab="",xlab="", beside=TRUE, col= terrain.colors(3), cex.axis=2.3, cex.names=2.3, mgp = c(3,1.8,1) )
legend(21, 1, c("Logistic Regression",  "Binary", "Naive Bayes"), bty = "n" , cex=2.3, fill=terrain.colors(3))
title(ylab = "F1-Measure", mgp = c(4.5, 0, 0), cex.lab=2.3)
par("mar"=c(5,4,4,1)+3) 

# _________________________________________________________________________________________________________________________________________________________________
# _________________________________________________________________________________________________________________________________________________________________

# Stratified sample agreement
# Cohen's kappa 
library(RPostgreSQL)
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, host='localhost', port='5432', dbname='comment_classification', user='evermal', password='')

# postgresql <- dbSendQuery(con, "select classification from significative_sample where classification in ('DESIGN') order by processedcommentid") #0.75862069
# postgresql <- dbSendQuery(con, "select classification from significative_sample where classification in ('IMPLEMENTATION') order by processedcommentid") #0.8461538
postgresql <- dbSendQuery(con, "select classification from significative_sample where classification in ('WITHOUT_CLASSIFICATION') order by processedcommentid") #0.988505747
# postgresql <- dbSendQuery(con, "select classification from significative_sample where classification in ('WITHOUT_CLASSIFICATION', 'DESIGN', 'IMPLEMENTATION') order by processedcommentid")
# postgresql <- dbSendQuery(con, "select classification from significative_sample order by processedcommentid") #0.81
reviewer1 <- fetch(postgresql, n=-1)
dim(reviewer1)
dbHasCompleted(postgresql)

library(RPostgreSQL)
library(psych)
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, host='localhost', port='5432', dbname='comment_classification', user='evermal', password='')
# postgresql <- dbSendQuery(con, "select reviewerclassification from significative_sample where processedcommentid in (select processedcommentid from significative_sample where classification = 'DESIGN' order by processedcommentid) order by processedcommentid")
# postgresql <- dbSendQuery(con, "select reviewerclassification from significative_sample where processedcommentid in (select processedcommentid from significative_sample where classification = 'IMPLEMENTATION' order by processedcommentid) order by processedcommentid")
postgresql <- dbSendQuery(con, "select reviewerclassification from significative_sample where processedcommentid in (select processedcommentid from significative_sample where classification = 'WITHOUT_CLASSIFICATION' order by processedcommentid) order by processedcommentid")
# postgresql <- dbSendQuery(con, "select reviewerclassification from significative_sample where processedcommentid in (select processedcommentid from significative_sample where classification in ('WITHOUT_CLASSIFICATION', 'DESIGN', 'IMPLEMENTATION') order by processedcommentid) order by processedcommentid")
# postgresql <- dbSendQuery(con, "select reviewerclassification from significative_sample order by processedcommentid")
reviewer2 <- fetch(postgresql, n=-1)
dim(reviewer2)
dbHasCompleted(postgresql)
xy.df <- data.frame(reviewer1,reviewer2)
ck <- cohen.kappa(xy.df)
ck
ck$agree
# __________________________________________________________________________________________________________________________________________________________________________________________________________________________

# Measuring P-value for table 2

nlp_based_design = c(0.517,0.814,0.601,0.470,0.744,0.509,0.492,0.731,0.783,0.540)
comment_patterns = c(0.237,0.107,0.264,0.231,0.227,0.342,0.282,0.194,0.620,0.175)
randon_classifier = c(0.044,0.144,0.037,0.034,0.193,0.037,0.077,0.072,0.123,0.055)

wilcox.test(nlp_based_design, comment_patterns) 0.0003248
wilcox.test(nlp_based_design, randon_classifier) 1.083e-05

nlp_based_requirent  = c(0.154,0.595,0.804,0.381,0.476,0.091,0.321,0.237,0.435,0.541) 
comment_patterns_req = c(0.000,0.000,0.117,0.000,0.000,0.000,0.000,0.148,0.409,0.000)
randon_classifier_req= c(0.006,0.079,0.013,0.007,0.041,0.003,0.007,0.005,0.043,0.014)

wilcox.test(nlp_based_requirent, comment_patterns_req) 0.001029
wilcox.test(nlp_based_requirent, randon_classifier_req) 0.0001817

# __________________________________________________________________________________________________________________________________________________________________________________________________________________________