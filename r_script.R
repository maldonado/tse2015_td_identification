
# generate figure to compare precision, recall and f1measure of all projects
mydata <- data.frame(Ant= c(0.597,0.389,0.471,0.55 ,0.082,0.142),Jmeter= c(0.848,0.601,0.704,0.733,0.058,0.108),ArgoUML= c(0.769,0.875,0.819,0.790,0.020,0.040),Columba= c(0.862,0.444,0.586,0.833,0.033,0.065),EMF= c(0.521,0.321,0.397,0.5  ,0.048,0.087),Hibernate= c(0.882,0.569,0.692,0.909,0.063,0.118),JEdit= c( 0.84,0.321,0.465,0.869,0.156,0.264),JFreeChart= c(0.689,0.397,0.503,0.833,0.022,0.044),JRuby= c(0.824,0.767,0.795,0.764,0.041,0.078),SQuirrel= c(0.598,0.498,0.543,0.5  ,0.023,0.044))
barplot(as.matrix(mydata),  ylab="Percentage",  ylim=c(0, 1), beside=TRUE, col= terrain.colors(6))
legend("topright", c("Precision", "Recall", "F1","Baseline P", "Baseline R", "Baseline F1"), cex=0.8, fill=terrain.colors(6))

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

# generate comparison between td classified and random measured
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%ant%' and category = 'DESIGN' and classificationid=3  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%jmeter%' and category = 'DESIGN' and classificationid=3  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%argo%' and category = 'DESIGN' and classificationid=3  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%columba%' and category = 'DESIGN' and classificationid=3  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%emf%' and category = 'DESIGN' and classificationid=3  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%hibernate%' and category = 'DESIGN' and classificationid=3  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%jEdit%' and category = 'DESIGN' and classificationid=3  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%jfreechart%' and category = 'DESIGN' and classificationid=3  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%jruby%' and category = 'DESIGN' and classificationid=3  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%sql12%' and category = 'DESIGN' and classificationid=3  order by 1,2")


postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%ant%' and category = 'IMPLEMENTATION' and classificationid=3  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%jmeter%' and category = 'IMPLEMENTATION' and classificationid=3  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%argo%' and category = 'IMPLEMENTATION' and classificationid=3  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%columba%' and category = 'IMPLEMENTATION' and classificationid=3  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%emf%' and category = 'IMPLEMENTATION' and classificationid=3  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%hibernate%' and category = 'IMPLEMENTATION' and classificationid=3  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%jEdit%' and category = 'IMPLEMENTATION' and classificationid=3  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%jfreechart%' and category = 'IMPLEMENTATION' and classificationid=3  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%jruby%' and category = 'IMPLEMENTATION' and classificationid=3  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%sql12%' and category = 'IMPLEMENTATION' and classificationid=3  order by 1,2")

library(RPostgreSQL)
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, host='localhost', port='5432', dbname='comment_classification', user='evermal', password='evermalton')
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%ant%' and category = 'IMPLEMENTATION' and classificationid=3  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%jmeter%' and category = 'IMPLEMENTATION' and classificationid=3  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%argo%' and category = 'IMPLEMENTATION' and classificationid=3  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%columba%' and category = 'IMPLEMENTATION' and classificationid=3  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%emf%' and category = 'IMPLEMENTATION' and classificationid=3  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%hibernate%' and category = 'IMPLEMENTATION' and classificationid=3  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%jEdit%' and category = 'IMPLEMENTATION' and classificationid=3  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%jfreechart%' and category = 'IMPLEMENTATION' and classificationid=3  order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%jruby%' and category = 'IMPLEMENTATION' and classificationid=3  order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%sql12%' and category = 'IMPLEMENTATION' and classificationid=3  order by 1,2")
data1 <- fetch(postgresql, n=-1)
dim(data1)
dbHasCompleted(postgresql)
plot(data1$projectstrainedwith, data1$classifiedf1*100, type="b",
     col="red", lty=2, pch=2, lwd=2,
     xlab="Projects used in training data", ylab="F1 measure",
     xlim=c(0, 10), ylim=c(0, 100))
lines(data1$projectstrainedwith, data1$classifiedrandomf1*100, type="b", pch=22, col="blue", lty=2)
legend(8, 99, c("Classified", "Random"), col= c("red", "blue"), pch = c(2, 22))
