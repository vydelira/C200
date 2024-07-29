
ta = float(input("What is the temperature? "))
V = float(input("What is the wind speed? "))
Twc = float((34.74+(0.6215*ta)) - (35.75*(V**0.16)) + ((0.4275*ta) * (V**0.16)))

print("The Windchill is:  " , Twc)
