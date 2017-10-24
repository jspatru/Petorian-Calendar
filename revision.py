#Every variable is measured in an SI second
#
import math
secondsInADay = 86164.0916 #23.9344699 hours or 0.99726958 mean solar days
secondsInAYear = 31558149.5 #All Sidereal
sdaysInAYear = secondsInAYear/secondsInADay #366.256394259
epoch = secondsInAYear/73 #432303.417808, one sidereal year divided by 73
#5.01721088026 parts are in an epoch
part = 432303.417808/5.01721088026
p=4
e=72
lc1=0
lc2=0
while p >= 4:
    print part*p
    p=p+1
