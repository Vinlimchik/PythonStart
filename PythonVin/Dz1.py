x = 0
num = input("Enter a random number: ")
while num != ("exit"):
    num = input("Enter a random number: ")
for value in num:
    if value % 2 == 0:
        x = x + 1
        print(x)