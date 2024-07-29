def max(x, y, z) :
    if (x > y) and (x > z) :
        return x
    elif (y > x) and (y > z) :
        return y
    elif (z > x) and (z > y) :
          return z
    else: 
        return x

print(max(4, 5, 128379827984))


def min(x, y, z) :
   if (x < y) and (x < z) :
        return x
   elif (y < x) and (y < z) :
        return y
   elif (z < x) and (z < y) :
       return z
   else:
       return x

print(min(4, 1, 1))


def max(x, y, z) :
    if ((x + y) > (x + z)) and ((x + y) > (y + z)) :
        return (x + y)
    elif ((y + z) > (y + x)) and (( y + z) > (x + z)) :
        return(y + z)
    elif (( z + x) > (z + y)) and ((z + x) > (x + y)) :
        return(x + z)
    else:
        return x
  
   
print(max(2, 6, 1))

def min(x, y, z) :
    if ((x + y) < (x + z)) and ((x + y) < (y + z)) :
        return (x + y)
    elif ((y + z) < (y + x)) and ((y + z) < (x + z)) :
        return(y + z)
    elif ((z + x) < (z + y)) and ((z + x) < (x + y)) :
        return(x + z)
    else:
        return x

print(min(4, 5, 6))



ls = [1,2,3]

def maxList(aList) :
    x = aList[0]
    for i in range(len(aList)):
        if(aList[i] > x):
            x = aList[i]
    return x

print(maxList(ls))


ls = [1, 2, 3]

def minList(aList) :
    x = aList[0]
    for i in range(len(aList)):
        if(aList[i] < x):
            x= aList[i]
    return x
print(minList(ls))
  