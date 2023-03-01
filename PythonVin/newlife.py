#secret number = "8"

num = input("Enter the secret number :")
while num != 8:
    print("Unright!")
    if int(num) > 8:
        print("The secret number less")
        num = input("Enter the secret number :")
    
    if int(num) < 8:
        print("the secret number larger")
        num = input("Enter the secret number :")
    
    if int(num) == 8:
        print("Absolutely right")
        num = input("Enter the new secret number :")
