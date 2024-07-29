for i in range(0, 4):
    print(i)


for move in range(0, 4):
    print(move * 1.0)


for i in range(0, 5):
    print(i)


for kitty in range(0, 3):
    print(kitty)


for Supercalifragilisticexpialidocious in range(0, 1):
    print(Supercalifragilisticexpialidocious)    #This one had a spelling error


#Invert '*' triangle 
for i in range(0,5):
    print('*' *(5-i), end="")
    print()


for i in range(11, 0, -2):
    print('' *int((12-i)/2) + '*'*i, end="")
    print()


#find sum (bounded loop)
sum = 0
n = (10)
for i in range(1, n + 1):
    sum = sum + i**2
print(sum)


#Donations
donations = [10, 12, 0.75, 5.23, 25.35,14.53, 15.99, 8.00, 8.01, 0.25]
sum = 0
for i in donations:
    sum = sum + i 

if sum >= 100:
    print("Total money donated is", sum, " Donations will be doubled to", sum*2)

else:
    print("Donations will not be doubled", sum)