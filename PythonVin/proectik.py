nom = input("select operation: +, -, *, /, //, !, √^2, √^3, ^n, save, exit, save and exit: ")
num = 1
nim = 1
nym = 1
ibm = 1
x = 0
y = 0
u = 0
i = 0
o = 0
p = 0
sqrt = 0
cbrt = 0
result = 0
r = 0

while nom != "exit":

#+
    if nom == "+":
        num = input("Enter a first number: ")
        nim = input("Enter a second number: ")
        x = int(num) + int(nim)
        int(num) + int(nim)
        print(x)
        nom = input("select operation: +, -, *, /, //, !, √^2, √^3, ^n, save, exit: ")

#-
    elif nom =="-":
        num = input("Enter a first number: ")
        nim = input("Enter a second number: ")
        y = int(num) - int(nim)
        int(num) - int(nim)
        print(y)
        nom = input("select operation: +, -, *, /, //, !, √^2, √^3, ^n, save, exit: ")
        
#*
    elif nom == "*":
        num = input("Enter a first number: ")
        nim = input("Enter a second number: ")
        u = int(num) * int(nim)
        int(num) * int(nim)
        print(u)
        nom = input("select operation: +, -, *, /, //, !, √^2, √^3, ^n, save, exit: ")

#/
    elif nom == "/":
        num = input("Enter a first number: ")
        nim = input("Enter a second number: ")
        i = int(num) / int(nim)
        int(num) / int(nim)
        print(i)
        nom = input("select operation: +, -, *, /, //, !, √^2, √^3, ^n, save, exit: ")

#//
    elif nom == "//":
        num = input("Enter a first number: ")
        nim = input("Enter a second number: ")
        o = int(num) // int(nim)
        int(num) // int(nim)
        print(o)
        nom = input("select operation: +, -, *, /, //, !, √^2, √^3, ^n, save, exit: ")

#n!
    elif nom == "!":
        nym = input("Enter a number: ")
        p = 1
        for step in range (1,int(nym)+1):
            p = p * step
        print(p)
        nom = input("select operation: +, -, *, /, //, !, √^2, √^3, ^n, save, exit: ")
        
#√^2
    elif nom == "√^2":
        nym = input("Enter a number: ")
        sqrt = int(nym) ** (0.5)
        print(sqrt)
        nom = input("select operation: +, -, *, /, //, !, √^2, √^3, ^n, save, exit: ")

#√^3
    elif nom == "√^3":
        nym = input("Enter anumber: ")
        cbrt = int(nym) ** (1./3.)
        print(cbrt)
        nom = input("select operation: +, -, *, /, //, !, √^2, √^3, ^n, save, exit: ")
    
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
        nom = input("select operation: +, -, *, /, //, !, √^2, √^3, ^n, save, exit: ")
    
#save
    elif nom == "save":
        file = open("meow.txt",'w')
        if x != 0:
            file.write(str(x))
            file.write(" - ")
            file.write("addition result")
            file.write("\n")
        
        if y != 0:
            file.write(str(y))
            file.write(" - ")
            file.write("subtraction result")
            file.write("\n")
        
        if u != 0:
            file.write(str(u))
            file.write(" - ")
            file.write("multiplication result")
            file.write("\n")
        
        if i != 0:
            file.write(str(i))
            file.write(" - ")
            file.write("division result")
            file.write("\n")
        
        if o != 0:
            file.write(str(o))
            file.write(" - ")
            file.write("result of integer division")
            file.write("\n")
        
        if p != 0:
            file.write(str(p))
            file.write(" - ")
            file.write("factorial")
            file.write("\n")
        
        if sqrt != 0:
            file.write(str(sqrt))
            file.write(" - ")
            file.write("square root")
            file.write("\n")
        
        if cbrt != 0:
            file.write(str(cbrt))
            file.write(" - ")
            file.write("cube root")
            file.write("\n")
            
        if result != 0:
            file.write(str(result))
            file.write(" - ")
            file.write("degree")
            file.write("\n")
            
        file.close()
        nom = input("select operation: +, -, *, /, //, !, √^2, √^3, ^n, save, exit: ")
        
#other
    elif nom != "+" or "-" or "*" or "/" or "//" or "!" or "√:2" or "√^3" or  "^n" or "save"  or "exit":
        print("Wrong!")
        nom = input("select operation: +, -, *, /, //, !, √^2, √^3, ^n, save, exit: ")
        
if nom == "exit":
    r = input("Do you want to save calculation?: ")
    if r == "yes":
        file = open("meow.txt",'w')
        if x != 0:
            file.write(str(x))
            file.write(" - ")
            file.write("addition result")
            file.write("\n")
        
        if y != 0:
            file.write(str(y))
            file.write(" - ")
            file.write("subtraction result")
            file.write("\n")
        
        if u != 0:
            file.write(str(u))
            file.write(" - ")
            file.write("multiplication result")
            file.write("\n")
        
        if i != 0:
            file.write(str(i))
            file.write(" - ")
            file.write("division result")
            file.write("\n")
        
        if o != 0:
            file.write(str(o))
            file.write(" - ")
            file.write("result of integer division")
            file.write("\n")
        
        if p != 0:
            file.write(str(p))
            file.write(" - ")
            file.write("factorial")
            file.write("\n")
        
        if sqrt != 0:
            file.write(str(sqrt))
            file.write(" - ")
            file.write("square root")
            file.write("\n")
        
        if cbrt != 0:
            file.write(str(cbrt))
            file.write(" - ")
            file.write("cube root")
            file.write("\n")
            
        if result != 0:
            file.write(str(result))
            file.write(" - ")
            file.write("degree")
            file.write("\n")
            
        file.close()
    else:
        print("ok, meow")
