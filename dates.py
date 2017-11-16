#Every variable is measured in an SI second
#As of January 1, 2017 CE, we were about 29.691992871777067 parts behind schedule.
import math
from datetime import *
import time
import calendar
secondsInADay = 86164.0916 #23.9344699 hours or 0.99726958 mean solar days
secondsInAYear = 31558149.5 #All Sidereal
ephemerisDay = 86400
sdaysInAYear = secondsInAYear/secondsInADay #366.256394259
epoch = secondsInAYear/73 #432303.417808, one sidereal year divided by 73
delay = 2523249.324
#5.01721088026 parts are in an epoch
part = epoch/5 #86460.6835616, or 24.01685654488889 hours
e=0
lc1=1
lc2=1
now = datetime.now()
d = date(datetime.now().year, 01, 01)
bang = calendar.timegm(d.timetuple())
while e <= 72:
  p=0
  print("Epoch " + str(lc1) + ": " + str(datetime.fromtimestamp(epoch*e-delay+bang)) + " UTC") #946684800 
  e=e+1
  lc1=lc1+1
  while p <= 4:
    #print datetime.datetime(2000, 01, 01)
    #print (datetime.fromtimestamp(part*(lc2-1)-delay).strftime("%A, %B %d %I:%M:%S"))
    print("\tPart " + str(p+1) + ": " + str(datetime.fromtimestamp(part*(lc2-1)-delay+bang)) + " UTC")
    p=p+1
    lc2=lc2+1
    #.strftime("%Y, %A, %B %d %I:%M:%S") for the date spelled out
#print("\tYEAR END: " + str(secondsInAYear-delay))
#2567190 seconds
#29 days, 4 hours, 54 minutes, 9.324000000022352 seconds; 2523249.324 seconds
#510 leap days since January 1, 45 BCE
#http://keisan.casio.com/exec/system/1295254517 <-- this link helped a lot
