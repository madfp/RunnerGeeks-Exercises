import sys

band = 0
tests = 0
for i in sys.stdin:
    if band == 0:
        tests = int(i)
        band = 1
    else:
        