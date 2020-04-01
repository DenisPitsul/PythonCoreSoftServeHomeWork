width = int(input("Input the width of rectangle: "))
height = int(input("Input the height of rectangle: "))
flag = False
while not flag:
    borderChar = str(input("Input character for border: "))
    if len(borderChar) == 1:
        flag = True
    else:
        print("You have to input single character")
        continue
flag = False
while not flag:
    contentChar = str(input("Input character for content: "))
    if len(contentChar) == 1:
        flag = True
    else:
        print("You have to input single character")
        continue

for i in range(width):
    for j in range(height):
        if (i == 0 or j == 0 or j == height - 1 or i == width - 1):
            print(borderChar, end='')
        else:
            print(contentChar, end='')
    print('')