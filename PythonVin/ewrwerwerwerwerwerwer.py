o = "0"
x = 0
y = 0
num = 0


pole = [["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]]

pole[x][y] = o

for i in pole:
    for t in i:
        print(t,end='')
    print()

while num!= "exit":
    if num == "right":
        y = y + 1
        pole[x][y] = o
        num = input("Enter command: right, left, up, down or exit: ")
        for i in pole:
            for t in i:
                print(t,end='')
        print()

    if num == "left":
        y = y - 1
        pole[x][y] = o
        num = input("Enter command: right, left, up, down or exit: ")
        for i in pole:
            for t in i:
                print(t,end='')
        print()

    if num == "up":
        x = x + 1
        pole[x][y] = o
        num = input("Enter command: right, left, up, down or exit: ")
        for i in pole:
            for t in i:
                print(t,end='')
        print()
    
    if num == "down":
        x = x - 1
        pole[x][y] = o
        num = input("Enter command: right, left, up, down or exit: ")
        for i in pole:
            for t in i:
                print(t,end='')
        print()

    if num != "right" or "left" or "up" or "down" or "exit":
        print("Wrong!")
        num = input("Enter command: right, left, up, down or exit: ")
        
if num == "exit":
    print("Arevouar, Shoshanna!")