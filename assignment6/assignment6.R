setwd('/Users/riccardo/Documents/personal/data-manipulation/datasci_course_materials/assignment6')
sea <- read.csv('seattle_incidents_summer_2014.csv', na.strings=c("NA","#DIV/0!",""))
x <- sea$Occurred.Date.or.Date.Range.Start
hr <- as.integer(substr(x, 12,13))
AP <- substr(x, 21, 22)
AP[AP=="PM"]=12
AP[AP=="AM"]=0
AP <- as.integer(AP)
sea$Hr24 <- as.factor(AP+hr)
plot(sea$Hr24)

library(plyr)
sea$Hr24 <- as.integer(sea$Hr24)
sea_evening <- subset(sea, sea$Hr24 >= 18 & sea$Hr24 <= 24, select=c(Offense.Type, Offense.Code))
frequency <- count(sea_evening, c('Offense.Type', 'Offense.Code'))
frequency <- arrange(frequency, desc(freq))
frequency <- subset(frequency, frequency$freq > 100)
frequency$Offense.Type <- factor(frequency$Offense.Type, levels = frequency$Offense.Type)
plot(x =frequency$Offense.Type,y=frequency$freq, las=2, cex.axis=0.5)

ptn = '.*ROBBERY.*?'
ndx <- grep(ptn, sea$Offense.Type, perl=T)
sea_robberies <- sea[ndx,]
sea_robberies$Hr24 <- as.factor(sea_robberies$Hr24)
plot(sea_robberies$Hr24)