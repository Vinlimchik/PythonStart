#Variables
move = 0
row = 0
column = 0

#Massive
field = [["[]","[]","[]"],
            ["[]","[]","[]"],
            ["[]","[]","[]"]]

field[row][column] = []

for line in field:
    for i in line:
        print(i,end="")
    print()

#Cycle

#Main
move = input("X or O: ")
row = input("Select row: ")
column = input("Select column: ")

#X[1,1]
if row == 1 and column == 1 and move == "X":
    field[row][column] = "X"
    
for line in field:
    for i in line:
        print(i,end="")
    print()
    
move = input("X or O: ")
row = input("Select row: ")
column = input("Select column: ")

#O[1,1]
if row == 1 and column == 1 and mve == "O":
    field[row][column] = "O"

    for line in field:
        for i in line:
            print(i,end="")
        print()

move = input("X or O: ")
row = input("Select row: ")
column = input("Select column: ")