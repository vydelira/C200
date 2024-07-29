import numpy as np

def xs(x):
    sum = 0
    for i in x:
        sum = sum + i
    return sum

def ys(y):
    sum = 0
    for i in y:
        sum = sum + i
    return sum

def xys(x,y):
    sum = 0
    for x,y in zip(x,y):
        sum = sum + (x*y)
    return sum

def xss(x):
    sum = 0
    for i in x:
        sum = sum + (i**2)
    return sum


def yss(y):
    sum = 0
    for i in y:
        sum = sum + (i**2)
    return sum
        


def r(x,y):
    n = len(x)
    z = float((n * xys(x,y)) - ((xs(x))*(ys(y)))) / ((((n*(xss(x))) - (xs(x))**2)) * (((n*(yss(y))) - (ys(y))**2)))**(.5)
    return z

a = np.array(range(12),int).reshape((6,2))

fm = open("studyhours.txt", 'r')

for i in range(6): 
    d = fm.readline().split(',') 
    a[i][0] = int(d[0]) 
    a[i][1] = int(d[1])

print("The correlation is: {0}.".format(r(a[:,[0]], a[:,[1]])))