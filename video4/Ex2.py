numberList = []
i = 1
while i <= 10:
    number = int(input("Input " + str(i) + " number: "))
    if number > 2:
        numberList.append(number)
    else:
        print("Number have to be more than 2!")
        i -= 1
    i += 1
count = 0
for number in numberList:
    if number % 5 == 0:
        count += 1
print("The number of numbers is a multiple of 5: {}".format(count))