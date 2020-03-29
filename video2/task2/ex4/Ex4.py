while True:
    seatNumber = input("Input the number of seat in the seat car(number should be in this range [1, 54]): ")
    if seatNumber.isnumeric() == False:
        print("It is have to be number!")
        continue

    seatNumber = int(seatNumber)
    if 0 < seatNumber < 55:
        if seatNumber < 37:
            if seatNumber % 2 == 0:
                print("The seat is top and in the compartment.")
            else:
                print("The seat is bottom and in the compartment")
        else:
            if seatNumber % 2 == 0:
                print("The seat is side and top.")
            else:
                print("The seat is side and bottom")
        break
    else:
        print("Number should be in this range [1, 54]")
        continue
