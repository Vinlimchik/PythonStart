nom = input("select operation: +, -, *, /, //, !, √^2, √^3, ^n, multitask, exit: ")
num = 1
nim = 1
nym = 1
ibm = 1

while nom != "exit":

#+
    if nom == "+":
        num = input("Enter a first number: ")
        nim = input("Enter a second number: ")
        x = int(num) + int(nim)
        int(num) + int(nim)
        print(x)
        nom = input("select operation: +, -, *, /, //, !, √^2, √^3, ^n, multitask, exit: ")

#-
    elif nom =="-":
        num = input("Enter a first number: ")
        nim = input("Enter a second number: ")
        y = int(num) - int(nim)
        int(num) - int(nim)
        print(y)
        nom = input("select operation: +, -, *, /, //, !, √^2, √^3, ^n, multitask, exit: ")
        
#*
    elif nom == "*":
        num = input("Enter a first number: ")
        nim = input("Enter a second number: ")
        u = int(num) * int(nim)
        int(num) * int(nim)
        print(u)
        nom = input("select operation: +, -, *, /, //, !, √^2, √^3, ^n, multitask, exit: ")

#/
    elif nom == "/":
        num = input("Enter a first number: ")
        nim = input("Enter a second number: ")
        i = int(num) / int(nim)
        int(num) / int(nim)
        print(i)
        nom = input("select operation: +, -, *, /, //, !, √^2, √^3, ^n, multitask, exit: ")

#//
    elif nom == "//":
        num = input("Enter a first number: ")
        nim = input("Enter a second number: ")
        o = int(num) // int(nim)
        int(num) // int(nim)
        print(o)
        nom = input("select operation: +, -, *, /, //, !, √^2, √^3, ^n, multitask, exit: ")

#n!
    elif nom == "!":
        nym = input("Enter a number: ")
        p = 1
        for step in range (1,int(nym)+1):
            p = p * step
            print(p)
        nom = input("select operation: +, -, *, /, //, !, √^2, √^3, ^n, multitask, exit: ")
        
#√^2
    elif nom == "√^2":
        nym = input("Enter a number: ")
        sqrt = int(nym) ** (0.5)
        print(sqrt)
        nom = input("select operation: +, -, *, /, //, !, √^2, √^3, ^n, multitask, exit: ")

#√^3
    elif nom == "√^3":
        nym = input("Enter anumber: ")
        cbrt = int(nym) ** (1./3.)
        print(cbrt)
        nom = input("select operation: +, -, *, /, //, !, √^2, √^3, ^n, multitask, exit: ")
    
#^n
    elif nom == "^n":
        nym = input("Select degree: ")
        ibm = input("Enter a number: ")
        d = nym
        t = int(ibm)
        result = 1
        for i in range(1,int(d)+1):
            result = result * t
        print(result)
        nom = input("select operation: +, -, *, /, //, !, √^2, √^3, ^n, multitask, exit: ")
    
#multitask
    elif nom == "multitask":
        nym = input("Enter first number: ")
        nom = input("Enter first operation: +, -, *, /, //, !, √^2, √^3, ^n: ")
        nim = input("Enter second number: ")
        num = input("Enter second operation: +, -, *, /, //, !, √^2, √^3, ^n: ")
        result = int(nym) + int(num)
    
#other
    elif nom != "+" or "-" or "*" or "/" or "//" or "!" or "√" or "^n" or "exit":
        print("Wrong!")
        nom = input("select operation: +, -, *, /, //, !, √^2, √^3, ^n, multitask, exit: ")
        
if nom == "exit":
    print("meow")
