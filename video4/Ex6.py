positiveNumbersCount = 0
negativeNumbersCount = 0
print('Input 0 to finish the program')
while True:
    number = float((input("Input number: ")))
    if number > 0:
        positiveNumbersCount += 1
    elif number < 0:
        negativeNumbersCount += 1
    else:
        break
sumPositiveAndNegativeNumbersCounts = positiveNumbersCount + negativeNumbersCount
positiveNumbersPercentage = positiveNumbersCount * 100 / sumPositiveAndNegativeNumbersCounts
negativeNumbersPercentage = negativeNumbersCount * 100 / sumPositiveAndNegativeNumbersCounts
print('{}% of positive numbers, {}% of negative numbers'.format(round(positiveNumbersPercentage, 2), round(negativeNumbersPercentage, 2)))