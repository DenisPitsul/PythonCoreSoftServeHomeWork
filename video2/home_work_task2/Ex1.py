number = int(input("Input natural number: "))

if number % 2 == 0:
    print("Number " + str(number) + " is even")
    if number%4 == 0:
        print("Number " + str(number) + " is a multiple of 4")
    else:
        print("Number " + str(number) + " is not a multiple of 4")
else:
    print("Number " + str(number) + " is odd")
