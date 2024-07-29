#Celcius to Farenheit
def celcius_to_fahrenheit(celcius, fahrenheit):
    fahrenheit = ((celcius * (9/5)) + 32)
    return fahrenheit

celcius = float(input("Temperature in degrees celcius: "))
fahrenheit = ((celcius * (9/5)) + 32) 

str(print(celcius_to_fahrenheit(celcius, fahrenheit), "Fahrenheit"))




#Conversion Function
def conversion(temperature):
    fahrenheit = (((temperature * (9/5)) + 32))
    return fahrenheit

temperature = float(input("Temperature in degrees celcius: "))

if conversion(temperature) < 45:
    print("Wear a coat!")
elif conversion(temperature) > 90:
    print("Stay hydrated!") 
elif conversion(temperature) >=45 and conversion(temperature) <=90:
    print("Weather is good, wear no jacket or light jacket. Have fun!")


#Extra Credit
def conv(temperature, kind):
    if (kind == 0):
        temperature = 5/9 * (temperature - 32)
        return temperature
    elif (kind == 1):
        temperature = (temperature * (9/5)) + 32
        return temperature
    return temperature

temperature = float(input("Temperature: "))
kind = float(input("Input 0 for temperature in Celcius or enter 1 for temperature in Farenheit: "))
print(conv(temperature, kind))