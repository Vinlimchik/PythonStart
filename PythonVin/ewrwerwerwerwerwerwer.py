#Variables
o = "0"
x = 0
y = 0
num = 0

#massive
field = [["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]]

field[x][y] = o

for line in field:
    for i in line:
        print(i,end='')
    print()
num = input("Enter command: w, a, s, d or exit: ")

#Cycle
while num!= "exit":
    
#W
    if num == "w":
        if x > 0:
            x = x - 1
            field[x][y] = o
            field[x+1][y] = "*"
        else:
            print("Wrong!")
        field[x][y] = o
        field[x+1][y] = "*"
        for line in field:
            for i in line:
                print(i,end='')
            print()
        num = input("Enter command: w, a, s, d or exit: ")

#A
    if num == "a":
        if y > 0:
            y = y - 1
            field[x][y] = o
            field[x][y+1] = "*"
        else:
            print("Wrong!")
        for line in field:
            for i in line:
                print(i,end='')
            print()
        num = input("Enter command: w, a, s, d or exit: ")

#S  
    if num == "s":
        if x < 9:
            x = x + 1
            field[x][y] = o
            field[x-1][y] = "*"
        else:
            print("Wrong!")
        for line in field:
            for i in line:
                print(i,end='')
            print()
        num = input("Enter command: w, a, s, d or exit: ")

#D
    if num == "d":
        if y < 9:
            y = y + 1
            field[x][y] = o
            field[x][y-1] = "*"
        else:
            print("Wrong!")
        for line in field:
            for i in line:
                print(i,end='')
            print()
        num = input("Enter command: w, a, s, d or exit: ")
        
#Exit
if num == "exit":
    print("Arevouar, Shoshanna!")
