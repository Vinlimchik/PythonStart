challenge_list = ["go to walk with dog", "read book"]

num = input("Choose a command: +, - , show element, show all list: ")
nim = 0
nym = 0
nom = 0

while num != "show all list": 
    if num == "+":
        nim = input("Enter a new element: ")
        challenge_list.append(nim)
        num = input("Choose a command: +, - , show element, show all list: ")
        
    elif num == "-":
        nym = input("Name the index or title of the element you want to delete: ")
        for i in challenge_list(len(challenge_list)):
            if challenge_list[i] == nym:
                    challenge_list.pop(int(nym))
                    del challenge_list[int(nym)]
        #challenge_list.pop(int(nym))
        #del challenge_list[int(nym)]
        num = input("Choose a command: +, - , show element, show all list: ")
    
    elif num == "show element":
        nom = input("Enter index what element you want to see: " )
        print(challenge_list[int(nom)])
        num = input("Choose a command: +, - , show element, show all list: ")
        
    elif num != "+, - , show element, show all list: ":
        print("Wrong!")
        num = input("Choose a command: +, - , show element, show all list: ")
        
if num == "show all list":
    print(challenge_list)