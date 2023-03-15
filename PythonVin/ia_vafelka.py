nom = input("select operation: +, -, *, /, //, exit: ")

while (nom == "exit"):
    print("it's all folks")
num = input("first number: ")
nim = input("second number: ")

x = int(num) + int(nim)
y = int(num) - int(nim)
u = int(num) * int(nim)
i = int(num) / int(nim)
o = int(num) // int(nim)


if (nom == "+"):
    int(num) + int(nim)
    print(x)
    nom = input("select operation: +, -, *, /, //, exit: ")
    
if (nom =="-"):
    int(num) - int(nim)
    print(y)
    nom = input("select operation: +, -, *, /, //, exit: ")
    
if (nom == "*"):
    int(num) * int(nim)
    print(u)
    nom = input("select operation: +, -, *, /, //, exit: ")
    
if (nom == "/"):
    int(num) / int(nim)
    print(i)
    nom = input("select operation: +, -, *, /, //, exit: ")

if (nom == "//"):
    int(num) // int(nim)
    print(o)
    nom = input("select operation: +, -, *, /, //, exit: ")

