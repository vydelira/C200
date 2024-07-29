I = float(input("What is your income? "))

if  ( 0 <= I <= 9075 ) :
    tax = (0 + .1 * (I - 0 ))
    print ("Amount you owe in Federal Taxes: ", tax)

elif ( 9076 <= I <= 36900 ):
    tax = ( 907.50 + .15 * (I - 9075 ))
    print ("Amount you owe in Federal Taxes: ", tax)

elif ( 36901 <= I <= 89350 ):
    tax = ( 5081.25 + .25 * (I - 36900 ))
    print ("Amount you owe in Federal Taxes: ", tax)

elif ( 89351 <= I <= 89350 ):
    tax = ( 18193.75 + .28 * (I - 89350 ))
    print ("Amount you owe in Federal Taxes: ", tax)

elif ( 186351 <= I <= 405100 ):
    tax = ( 45353.75 + .33 * (I - 186350 ))
    print ("Amount you owe in Federal Taxes: ", tax)

elif ( 405101 <= I <= 406750 ):
    tax = ( 117541.25 + .35 * (I - 405100 ))
    print ("Amount you owe in Federal Taxes: ", tax)

elif ( I >= 406751 ):
    tax = ( 118118.75 + .396 * (I - 406750 ))
    print ("Amount you owe in Federal Taxes: ", tax)


