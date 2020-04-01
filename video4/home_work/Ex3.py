print("Таблиця множення")
for i in range(0, 10):
    if i == 0:
        print(" ", end='\t')
    else:
        print("{}".format(i), end="\t")
print("\n  ------------------------------------")
for i in range(1, 10):
    print("{}|".format(i), end='\t')
    for j in range(1, 10):
        print("{}".format(i * j), end='\t')
    print("")