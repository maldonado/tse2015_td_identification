
# generate figure to compare precision, recall and f1measure of all projects
mydata <- data.frame(Ant=c(70.89,11.94,9.7,7.46,0), Jmeter=c(84.26,5.86,5.86,3.2,0.8), ArgoUml=c(48.45,39.38,7.68,2.66,1.81), JFreeChart=c(84.01,11.41,4.10,0.45,0), Columba=c(42.71,45.71,4.40,2.03,5.42))
barplot(as.matrix(mydata),  ylab="Percentage",  ylim=c(0, 100), beside=TRUE, col=1, density=c(25,20,15,10,5), angle = c(15, 45, 100, 120, 160))
legend(23, 90, c("Design debt", "Requirement debt", "Defect debt","Test debt", "Documentation debt"), cex=0.8, fill=terrain.colors(5))


# generate comparison between td classified and random measured
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%ant%' and category = 'DESIGN' and trainingorder like 'decrescent%' order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%jmeter%' and category = 'DESIGN' and trainingorder like 'decrescent%' order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%argo%' and category = 'DESIGN' and trainingorder like 'decrescent%' order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%columba%' and category = 'DESIGN' and trainingorder like 'decrescent%' order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%emf%' and category = 'DESIGN' and trainingorder like 'decrescent%' order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%hibernate%' and category = 'DESIGN' and trainingorder like 'decrescent%' order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%jEdit%' and category = 'DESIGN' and trainingorder like 'decrescent%' order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%jfreechart%' and category = 'DESIGN' and trainingorder like 'decrescent%' order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%jruby%' and category = 'DESIGN' and trainingorder like 'decrescent%' order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%sql12%' and category = 'DESIGN' and trainingorder like 'decrescent%' order by 1,2")


postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%ant%' and category = 'IMPLEMENTATION' and trainingorder like 'decrescent%' order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%jmeter%' and category = 'IMPLEMENTATION' and trainingorder like 'decrescent%' order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%argo%' and category = 'IMPLEMENTATION' and trainingorder like 'decrescent%' order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%columba%' and category = 'IMPLEMENTATION' and trainingorder like 'decrescent%' order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%emf%' and category = 'IMPLEMENTATION' and trainingorder like 'decrescent%' order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%hibernate%' and category = 'IMPLEMENTATION' and trainingorder like 'decrescent%' order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%jEdit%' and category = 'IMPLEMENTATION' and trainingorder like 'decrescent%' order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%jfreechart%' and category = 'IMPLEMENTATION' and trainingorder like 'decrescent%' order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%jruby%' and category = 'IMPLEMENTATION' and trainingorder like 'decrescent%' order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%sql12%' and category = 'IMPLEMENTATION' and trainingorder like 'decrescent%' order by 1,2")

library(RPostgreSQL)
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, host='localhost', port='5432', dbname='comment_classification', user='evermal', password='evermalton')
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%ant%' and category = 'DESIGN' and trainingorder like 'decrescent%' order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%jmeter%' and category = 'DESIGN' and trainingorder like 'decrescent%' order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%argo%' and category = 'DESIGN' and trainingorder like 'decrescent%' order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%columba%' and category = 'DESIGN' and trainingorder like 'decrescent%' order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%emf%' and category = 'DESIGN' and trainingorder like 'decrescent%' order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%hibernate%' and category = 'DESIGN' and trainingorder like 'decrescent%' order by 1,2")
postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%jEdit%' and category = 'DESIGN' and trainingorder like 'decrescent%' order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%jfreechart%' and category = 'DESIGN' and trainingorder like 'decrescent%' order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%jruby%' and category = 'DESIGN' and trainingorder like 'decrescent%' order by 1,2")
# postgresql <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%sql12%' and category = 'DESIGN' and trainingorder like 'decrescent%' order by 1,2")
data1 <- fetch(postgresql, n=-1)
dim(data1)
dbHasCompleted(postgresql)
plot(data1$projectstrainedwith, data1$classifiedf1*100, type="b",
     col="red", lty=2, pch=2, lwd=2,
     xlab="Projects used in training data", ylab="F1 measure",
     xlim=c(0, 10), ylim=c(0, 100))
lines(data1$projectstrainedwith, data1$classifiedrandomf1*100, type="b", pch=22, col="blue", lty=2)
legend(8, 99, c("Classified", "Random"), col= c("red", "blue"), pch = c(2, 22))
