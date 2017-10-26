#Every variable is measured in an SI second
#
secondsInADay = 86164.0916 #23.9344699 hours or 0.99726958 mean solar days
secondsInAYear = 31558149.5 #All Sidereal
sdaysInAYear = secondsInAYear/secondsInADay #366.256394259
epoch = secondsInAYear/73 #432303.417808, one sidereal year divided by 73
#5.01721088026 parts are in an epoch
part = epoch/5 #86460.6835616
p=0
e=0
lc1=1
lc2=1
while e <= 72:
  print("Epoch " + str(lc1) + ": " + str(epoch*e))
  e=e+1
  lc1=lc1+1
  p=0
  while p <= 4:
      print("\tPart " + str(p+1) + ": " + str(part*lc2))
      p=p+1
      lc2=lc2+1
