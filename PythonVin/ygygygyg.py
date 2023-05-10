list = []
sum_positive = 0
sum_negative = 0
massive = " "
number = 0

while massive != "show":
    number = input("Enter a list items: ")
    list.append(float(number))
    massive = input("show elements?: ")
if massive == "show":
    for i in range(0,len(list)):
        if list[i] >= 0:
            sum_positive = sum_positive + 1
            print(sum_positive)
        if list[i] < 0:
            sum_negative = sum_negative + 1
            print(sum_negative)