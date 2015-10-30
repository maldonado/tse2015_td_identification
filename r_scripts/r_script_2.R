mydata <- data.frame(Ant=c(0.597,0.389,0.471,0.023,0.5,0.045),Jmeter=c(0.848,0.601,0.704,0.04 ,0.5,0.075),ArgoUML=c(0.769,0.875,0.819,0.089,0.5,0.151),Columba=c(0.862,0.444,0.586,0.020,0.5,0.038),EMF=c(0.521,0.321,0.397,0.018,0.5,0.035),Hibernate=c(0.882,0.569,0.692,0.136,0.5,0.214),JEdit=c( 0.84,0.321,0.465,0.019,0.5,0.037),JFreeChart=c(0.689,0.397,0.503,0.043,0.5,0.080),JRuby=c(0.824,0.767,0.795,0.075,0.5,0.131),SQuirrel=c(0.598,0.498,0.543,0.029,0.5,0.055))
barplot(as.matrix(mydata),  ylab="Percentage",  ylim=c(0, 1), beside=TRUE, col=1, density=c(13,8,8,3,3,3), angle = c(0, 50, 90, 140, 180, 185))
legend("topright", c("Precision", "Recall", "F1 measure","Rnd Precision", "Rnd Recall", "Rnd F1 measure"), cex=1.3, col=1, density=c(18,13,13,8,8,8), angle = c(0, 50, 90, 140, 180, 185) , bty="y", seg.len=0.5)

mydata <- data.frame(Ant=c(0.597,0.389,0.471,0.023,0.5,0.045) * 100 ,Jmeter=c(0.848,0.601,0.704,0.04 ,0.5,0.075) * 100 ,ArgoUML=c(0.769,0.875,0.819,0.089,0.5,0.151) * 100 ,Columba=c(0.862,0.444,0.586,0.020,0.5,0.038) * 100 ,EMF=c(0.521,0.321,0.397,0.018,0.5,0.035) * 100 ,Hibernate=c(0.882,0.569,0.692,0.136,0.5,0.214) * 100 ,JEdit=c( 0.84,0.321,0.465,0.019,0.5,0.037) * 100 ,JFreeChart=c(0.689,0.397,0.503,0.043,0.5,0.080) * 100 ,JRuby=c(0.824,0.767,0.795,0.075,0.5,0.131) * 100 ,SQuirrel=c(0.598,0.498,0.543,0.029,0.5,0.055) * 100))
barplot(as.matrix(mydata),  ylab="Percentage",  ylim=c(0, 10), beside=TRUE, col=1, density=c(13,8,8,3,3,3), angle = c(0, 50, 90, 140, 180, 185))
legend(23, 92, c("Precision", "Recall", "F1 measure","Rnd Precision", "Rnd Recall", "Rnd F1 measure"), cex=1.3, col=1, density=c(18,13,13,8,8,8), angle = c(0, 50, 90, 140, 180, 185) , bty="y", seg.len=0.5)

mydata <- data.frame(Ant=c(0.597,0.389,0.471,0.023,0.5,0.045),Jmeter=c(0.848,0.601,0.704,0.04 ,0.5,0.075),ArgoUML=c(0.769,0.875,0.819,0.089,0.5,0.151),Columba=c(0.862,0.444,0.586,0.020,0.5,0.038),EMF=c(0.521,0.321,0.397,0.018,0.5,0.035),Hibernate=c(0.882,0.569,0.692,0.136,0.5,0.214),JEdit=c( 0.84,0.321,0.465,0.019,0.5,0.037),JFreeChart=c(0.689,0.397,0.503,0.043,0.5,0.080),JRuby=c(0.824,0.767,0.795,0.075,0.5,0.131),SQuirrel=c(0.598,0.498,0.543,0.029,0.5,0.055))
barplot(as.matrix(mydata),  ylab="Percentage",  ylim=c(0, 1), beside=TRUE, col= terrain.colors(6) ,lwd = 1)
legend("topright", c("Precision", "Recall", "F1 measure","Rnd Precision", "Rnd Recall", "Rnd F1 measure"), cex=1.3, fill = terrain.colors(6) , bty="y", seg.len=0.5)




par(lwd = 2)
par(lty = 1)
mydata <- data.frame(Ant=c(0.597,  0.389,  0.471),Jmeter=c(0.848,  0.601,  0.704),ArgoUML=c(0.769,  0.875,  0.819),Columba=c(0.862,  0.444,  0.586),EMF=c(0.521,  0.321,  0.397),Hibernate=c(0.882,  0.569,  0.692),JEdit=c( 0.84,  0.321,  0.465),JFreeChart=c(0.689,  0.397,  0.503),JRuby=c(0.824,  0.767,  0.795),SQuirrel=c(0.598,  0.498,  0.543))
barplot(as.matrix(mydata),  ylab="Percentage",  ylim=c(0, 1), beside=TRUE, col= terrain.colors(3) )


par(lwd = 1)
par(lty = 5)
mydata <- data.frame(Ant=c(0.023,0.5,0.045),Jmeter=c(0.848,0.601,0.704,0.04 ,0.5,0.075),ArgoUML=c(0.769,0.875,0.819,0.089,0.5,0.151),Columba=c(0.862,0.444,0.586,0.020,0.5,0.038),EMF=c(0.521,0.321,0.397,0.018,0.5,0.035),Hibernate=c(0.882,0.569,0.692,0.136,0.5,0.214),JEdit=c( 0.84,0.321,0.465,0.019,0.5,0.037),JFreeChart=c(0.689,0.397,0.503,0.043,0.5,0.080),JRuby=c(0.824,0.767,0.795,0.075,0.5,0.131),SQuirrel=c(0.598,0.498,0.543,0.029,0.5,0.055))
barplot(as.matrix(mydata),  ylab="Percentage",  ylim=c(0, 1), beside=TRUE, col= gray.colors(3) )

par(lty = 1)
legend("topright", c("Precision", "Recall", "F1 measure","Rnd Precision", "Rnd Recall", "Rnd F1 measure"), cex=1.3, col= terrain.colors(6) , bty="y", seg.len=0.5)








