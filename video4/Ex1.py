import random

randomNumber = random.randint(1, 100)
attempt = 1
while attempt <= 10:
    number = int(input("Guess the number from 1 to 100: "))
    if 1 > number >= 100:
        print("input number from 1 to 100")
    elif number == randomNumber:
        break
    elif number > randomNumber:
        print("less ")
    elif number < randomNumber:
        print("more ")
    attempt += 1
if number == randomNumber:
    print("You guessed the number from {} attempts! Right number: {}".format(attempt, randomNumber))
else:
    print("You have not guessed the number! Right number: {}".format(randomNumber))