library(RPostgreSQL)
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, host='localhost', port='5432', dbname='comment_classification', user='evermal', password='evermalton')
mongoose <- dbSendQuery(con, "select projectname, projectstrainedwith, classifiedf1 , classifiedrandomf1 from classifier_results where projectname like '%ant%' and category = 'DEFECT' and trainingorder like 'decrescent%' order by 1,2")
data1 <- fetch(mongoose,n=-1)
dim(data1)
dbHasCompleted(mongoose)


plot(data1$projectstrainedwith, data1$classifiedf1*100, type="b",
     col="red", lty=2, pch=2, lwd=2,
     xlab="Projects used in training data", ylab="F1 measure",
     xlim=c(0, 10), ylim=c(0, 100))
lines(data1$projectstrainedwith, data1$classifiedrandomf1*100, type="b", pch=22, col="blue", lty=2)