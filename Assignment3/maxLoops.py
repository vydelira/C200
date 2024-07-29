#Problem #1: find largest value in a list
#for-loop
list = [2, 8, 32, 4, 64, 0, 6000]
def maxFor(x):
    max = x[0]
    for i in range (1, len(x)):
        if x[i] > max:
            max = x[i]
    return max
print(maxFor(list))


#while-loop
def maxWhile(x):
    max = x[0]
    i = 0
    while (i < len(x)):
        if x[i] > max:
            max = x[i]
        i = i + 1
    return max
print(maxWhile(list))


#Extra Credit: Recursive
def maxRec(x):
    if len(x) == 1:
        return x
    else:
        if x[0] <  x[1]:
            return maxRec(x[1:])
        else:
            return maxRec([x[0]] + x[2:])

            return (x[0], maxRec(x[1:]))
print(maxRec(list))


