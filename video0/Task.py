
while True:
    name = input("What is your name?")
    if name.isalpha() == False:
        print("Name should only consist of letters!")
        continue
    break
while True:
    city = input("Where are you live?")
    if city.isalpha() == False:
        print("City should only consist of letters!")
        continue
    break
while True:
    age = input("Input your age?")
    if age.isnumeric() == False:
        print("Age have to be number!")
        continue

    age = int(age)
    if age > 0:
        break
    else:
        print("Age have to be positive!")
    break

print("Hello {}, You live in {}, Your age is {}.".format(name, city, age))
