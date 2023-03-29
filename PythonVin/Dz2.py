x = 0
num = 343,567,980,456,101,53,78,90,21,32
for value in num:
    if value > 100 and value < 999:
        if value % 2 > 0 and value % 3 > 0:
            print(value)
