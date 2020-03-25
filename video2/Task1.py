fuelCapacity = float(input("Input fuel capacity: "))
fuelAmount = float(input("Input fuel amount: "))

if fuelCapacity*0.1 > fuelAmount:
    print("Red")
else:
    print("Green")