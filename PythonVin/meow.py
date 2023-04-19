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

num = input("Enter command: r, l, u, d or exit: ")

while num != "exit":
    if num == "r":
        y = y + 1
        pole[x][y] = o
        #y = "*"
        num = input("Enter command: r, l, u, d or exit: ")
        for i in pole:
            for t in i:
                print(t,end='')
            print()

    if num == "l":
        y = y - 1
        pole[x][y] = o
        #y = "*"
        num = input("Enter command: r, l, u, d or exit: ")
        for i in pole:
            for t in i:
                print(t,end='')
            print()

    if num == "u":
        x = x - 1
        pole[x][y] = o
        #x = "*"
        num = input("Enter command: r, l, u, d or exit: ")
        for i in pole:
            for t in i:
                print(t,end='')
            print()
    
    if num == "d":
        x = x + 1
        pole[x][y] = o
        #x = "*"
        num = input("Enter command: r, l, u, d or exit: ")
        for i in pole:
            for t in i:
                print(t,end='')
            print()

    #if num != "right" or "left" or "up" or "down" or "exit":
        #print("Wrong!")
        #num = input("Enter command: right, left, up, down or exit: ")
        
if num == "exit":
    print("Arevouar, Shoshanna!")