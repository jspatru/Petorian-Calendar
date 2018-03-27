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
y=0
lc1=0
lc2=1
today = datetime.now()
NewYear=datetime.fromtimestamp(-62135596800)#44365448.499986738
secondsSinceNewYear=today-NewYear
while lc1<=2021:
  ti=(-62135596800+secondsInAYear*lc1)
  print("Year "+str(lc1+1) + ")\t" + str(ti) + "\t" + str(datetime.fromtimestamp(ti))+" UTC")
  while e<=72:
    x=datetime.fromtimestamp(epoch*e-62135596800+secondsInAYear*lc1)
    print("\tEpoch " + str(e+1) + ": " + str(x) + " UTC")
    p=0
    while p<=4:
      u=datetime.fromtimestamp(epoch*e-62135596800+secondsInAYear*lc1+part*p)
      print("\t\tPart " + str(p+1) + ": " + str(u) + " UTC")
      p=p+1
    e=e+1
  lc1=lc1+1
  e=0
  #while e <= 72:
   # while y<=2019:
	  #x=datetime.fromtimestamp(epoch*e-62135596800)
	  #print("\tEpoch " + str(e) + ": " + str(x) + " UTC")
	  #p=0
	  #e=e+1
	  #lc1=lc1+1
	  #y=y+1
#-62135596800 January 1, 0001; 12:00 AM
