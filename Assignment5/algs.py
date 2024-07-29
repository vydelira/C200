#Problem 1: Problem Solving

list = [1,2,2,1,5,2,3,4,5,8,3]

def increase(x):
    a = [x[0]]
    longest = []
    
    for i in range(0, len(x) - 2):
        if x[i] <= x[i + 1]:
            a.append(x[i + 1])
        else:
            a = [x[i + 1]]

        if len(a) >= len(longest):
            longest = a
    if len(longest) < 2:
        longest = [] 
    return longest

print(increase(list))
 

#RunOfOnes
list = [1,1,1,1,1,0,1]

def runOfOnes(x):
    lst = []
    longest = []
    for i in x:
        if i == 1:
            lst.append(1)
        else:
            lst = []

        if len(lst) >= len(longest):
            longest = lst
    
    return len(longest)

print(runOfOnes(list))



#stringIntersection

def stringIntersection(str1, str2):
    x = ""
    for i in str1:
        if i in str2:
            x = x + i
    return(x)

print(stringIntersection("abcd325", "5tDEDc3"))