# FIND DISTANCE
# ask for speed in mi/hr and time in min
def myDistance(speed, time):

#if speed is in mi/hr and time is in min, then distance is mi/hr/min
    distance = speed * time
    return distance

speed = float(input("What is the speed (mi/hr)?"))
time = float(input("What is the time (in minutes)?"))

str(print(myDistance(speed, time), "mi/hr/min")) #question .....


#FIND SPEED
# ask for distance in miles and time in hours
def mySpeed(distance, time):
    speed = distance/time
    return speed

distance = float(input("What is the distance (miles)?"))
time = float(input("What is the time (in hours)?"))

str(print(mySpeed(distance, time), "mi/hr"))