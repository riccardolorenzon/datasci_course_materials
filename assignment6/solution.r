x <- sea$Occurred.Date.or.Date.Range.Start
hr <- as.integer(substr(x, 12,13))
AP <- substr(x, 21, 22)
AP[AP=="PM"]=12
AP[AP=="AM"]=0
AP <- as.integer(AP)
sea$Hr24 <- as.factor(AP+hr)
plot(sea$Hr24)
