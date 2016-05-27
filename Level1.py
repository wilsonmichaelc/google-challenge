#!/usr/bin/python

#x = [22.2, 46, 100.8]
#y = [23, 11.1, 50.4]

x = [2.2999999999999998, 15.0, 102.40000000000001, 3486.8000000000002]
y = [23.0, 150.0, 1024.0, 34868.0]

def answer(x, y):
    z = [min(x), min(y)]
    s = min(z)
    l = max(z)
    return int(round((l-s)/l*100))

print answer(x, y)
