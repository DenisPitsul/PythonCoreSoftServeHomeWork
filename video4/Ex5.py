import random
P = random.randint(1, 100)
H = random.randint(P, P + 100)
sumNumbersLessP = 0
prodNumbersMoreH = 1
numbersCountInRangeFromPToH = 0
print("Number P: {}".format(P))
print("Number H: {}".format(H))
while True:
    number = int(input('Input number '))
    if number == P or number == H:
        break
    if number < P:
        sumNumbersLessP += number
    if number > H:
        prodNumbersMoreH *= number
    if P < number < H:
        numbersCountInRangeFromPToH += 1
print("Sum of numbers less than P: {}".format(sumNumbersLessP))
print("Product of numbers more than H: {}".format(prodNumbersMoreH))
print("Count of numbers in range from P to H: {}".format(numbersCountInRangeFromPToH))