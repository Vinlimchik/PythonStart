nom = input("select operation: +, -, *, /, //, exit: ")
while (nom != "exit"):
    nom = input("select operation: +, -, *, /, //, exit: ")
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
    
    if (nom =="-"):
        int(num) - int(nim)
        print(y)
        
    if (nom == "*"):
        int(num) * int(nim)
        print(u)

    if (nom == "/"):
        int(num) / int(nim)
        print(i)

    if (nom == "//"):
        int(num) // int(nim)
        print(o)
        
print("it's all folks")
      

