#Every variable is measured in an SI second
#As of January 1, 2017 CE, we were about 29.691992871777067 parts behind schedule.
import math
import time
from datetime import *
secondsInADay = 86164.0916 #23.9344699 hours or 0.99726958 mean solar days
secondsInAYear = 31558149.5 #All Sidereal
ephemerisDay = 86400
z = datetime.now()
theYear = z.year
sdaysInAYear = secondsInAYear/secondsInADay #366.256394259
epoch = secondsInAYear/73 #432303.417808, one sidereal year divided by 73
delay = 2523249.324*1
#5.01721088026 parts are in an epoch
part = epoch/5 #86460.6835616, or 24.01685654488889 hours
p=0
e=0
lc1=1
lc2=1
today = datetime.now()
NewYear=datetime.fromtimestamp(epoch*e-delay+1483228800-18000+secondsInAYear*(theYear-2017))
secondsSinceNewYear=today-NewYear
while e <= 72:
	x=datetime.fromtimestamp(epoch*e-delay+1483228800-18000+secondsInAYear*(theYear-2017))
	print("Epoch " + str(lc1) + ": " + str(x) + " EST")
	p=0
	e=e+1
	lc1=lc1+1
	while p <= 4:
		y=datetime.fromtimestamp(part*(lc2-1)-delay+1483228800-18000+secondsInAYear*(theYear-2017))#.strftime("%A, %B %d %I:%M:%S") str(part*(lc2-1)-delay)
		print("\tPart " + str(p+1) + ": " + str(y) + " EST")
		p=p+1
		if NewYear+secondsSinceNewYear >= y:
			todaysPart=p
			todaysEpoch=lc1
		lc2=lc2+1
print("Today is "+str(todaysPart)+"."+str(todaysEpoch-1)+"."+str(theYear+9997)+".")
#print("\tYEAR END: " + str(secondsInAYear-delay))
#2567190 seconds
#29 days, 4 hours, 54 minutes, 9.324000000022352 seconds; 2523249.324 seconds

#3:57 PM, January 11, 2018 CE (Gregorian Calendar): The program has officially just corrected me about what part it is. I'm so proud.
