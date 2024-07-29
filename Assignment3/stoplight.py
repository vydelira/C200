import math
#1
def y(d, r, t):
    r = r/100
    y = d*(math.exp(1)**(r*t))
    return y

d = int(input("Enter the deposit amount: "))
r = int(input("Interest rate(%) : "))
t = int(input("Yield: "))

print(y(d, r, t))


#2
def N(n0, m, t):
    N = n0 * (math.exp(1)**(m * t))
    return N

n0 = int(input("Initial number of bacteria: "))
m = int(input("Growth rate per hour: "))
t = int(input("Time in hours: "))

print(N(n0, m, t))


#3
def rate(age):
    if (6 <= age <= 10):
        return 2
    elif (11 <= age <= 15):
        return 2.5
    elif (16 <= age <= 18):
        return 3
    else:
        return 4

def DWtime(w, r):
    DWtime = w/r
    return DWtime

age = int(input("What is your age? ")) 
w = int(input("Length of intersection in feet: "))
r = rate(age)

print("Your walking rate in ft/sec is: " + str(rate(age)))
print("The time (in seconds) it takes you to cross the intersection is: " + str(DWtime(w, r)))

#CONSOLE
console = DWtime(w, r) - 6
print("Everyone is given 6 seconds to cross. It will take you " + str(console) + " seconds to cross.")

if console > 6:
    print("DO NOT CROSS!")
else:
    print("You may cross")



