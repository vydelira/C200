#Tic Tac Toe
game = [['_', '_', '_'],['_', '_', '_'], ['_', '_', '_']]
moves = [[0, 0], [0, 1], [0, 2], [1, 2], [1, 1], [2, 2], [2, 0]]

for next in range(0, 6):
    if next % 2== 0:
        symbol = 'X'
    else: 
        symbol = 'O'
    game[moves[next][0]][moves[next][1]] = symbol
for row in game:
    print(row)
print()




#Bounded loop to find smallest value
x = [25, 2, 142, 0, 54, -1]
i = 0
kitty = x[0]
for i in x:
    if i < kitty:
        kitty = i
print("The smallest value in x is " + str(kitty))