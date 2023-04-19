nom = input("select operation: +, -, *, /, //, !, √, exit: ")
num = 1
nim = 1
nym = 1
while (nom == "exit"):
    print("it's all folks")

while nom != "exit":

    if nom == "+":
        num = input("Enter a first number: ")
        nim = input("Enter a second number: ")
        x = int(num) + int(nim)
        int(num) + int(nim)
        print(x)
        nom = input("select operation: +, -, *, /, //, !, √, exit: ")
    
    elif nom =="-":
        num = input("Enter a first number: ")
        nim = input("Enter a second number: ")
        y = int(num) - int(nim)
        int(num) - int(nim)
        print(y)
        nom = input("select operation: +, -, *, /, //, !, √, exit: ")
        
    elif nom == "*":
        num = input("Enter a first number: ")
        nim = input("Enter a second number: ")
        u = int(num) * int(nim)
        int(num) * int(nim)
        print(u)
        nom = input("select operation: +, -, *, /, //, !, √, exit: ")
        
    elif nom == "/":
        num = input("Enter a first number: ")
        nim = input("Enter a second number: ")
        i = int(num) / int(nim)
        int(num) / int(nim)
        print(i)
        nom = input("select operation: +, -, *, /, //, !, √, exit: ")

    elif nom == "//":
        num = input("Enter a first number: ")
        nim = input("Enter a second number: ")
        o = int(num) // int(nim)
        int(num) // int(nim)
        print(o)
        nom = input("select operation: +, -, *, /, //, !, √, exit: ")
    
    elif nom == "!":
        nym = input("Enter a number: ")
        p = 1
        for step in range (1,int(nym)+1):
            p = p * step
            print(p)
        nom = input("select operation: +, -, *, /, //, !, √, exit: ")
        
    elif nom == "√":
        nym = input("Enter a number: ")
        
        nom = input("select operation: +, -, *, /, //, !, √, exit: ")
            
    elif nom != "+" or "-" or "*" or "/" or "//" or "!" or "√" or "exit":
        print("Wrong!")
        nom = input("select operation: +, -, *, /, //, !, √, exit: ")
        
if nom == "exit":
    print("meooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooow")