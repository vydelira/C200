aList= [1, 2, 4, 8]

#sums all numbers on a list using a while loop
def sumListWhile(aList):
    counter = 0
    result = 0
    while counter < len(aList):
        result += aList[counter]
        counter += 1
    return result
print("The sum is: " + str(sumListWhile(aList)))


#multiply the numbers in a list using a for loop
def multiplyListfor(aList):
    result = 1
    for item in aList:
        result = result * item
    return result
print("The product of the list is: " + str(multiplyListfor(aList)))


#return the factorial of n using a while loop
def factorialWhileLoop(n):
    result = 1
    counter = 1
    while counter < n+1:
        result = result * counter
        counter = counter+1
    return result
print(factorialWhileLoop(5))

#extra credit. Add x to itself y times 2, 3 is 2+2+2
def multiplyWhile(x, y):
    result = 0
    counter = 0
    while counter < y:
        result = x + result
        counter = counter + 1
    return result
print (multiplyWhile(2, 3))
    
