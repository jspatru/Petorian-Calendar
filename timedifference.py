#Accounting for the 2567190 seconds of time change from 1 January, 45 BCE and 1 January, 2017 CE

#Every variable is measured in an SI second
#As of January 1, 2017 CE, we were about 29.691992871777067 parts behind schedule.
secondsInADay = 86164.0916 #23.9344699 hours or 0.99726958 mean solar days
secondsInAYear = 31558149.5 #All Sidereal
sdaysInAYear = secondsInAYear/secondsInADay #366.256394259
epoch = secondsInAYear/73 #432303.417808, one sidereal year divided by 73
#5.01721088026 parts are in an epoch
part = epoch/5 #86460.6835616, or 24.01685654488889 hours
p=0
e=0
lc1=1
lc2=1
while e <= 72:
  print("Epoch " + str(lc1) + ": " + str(epoch*e-2567190))
  e=e+1
  lc1=lc1+1
  p=0
  while p <= 4:
      print("\tPart " + str(p+1) + ": " + str(part*lc2-2567190))
      p=p+1
      lc2=lc2+1
      #2567190 seconds
