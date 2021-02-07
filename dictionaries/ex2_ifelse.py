i = 2
j = 1
while i < 13:
    print("  [ ", i, " ]")
    while j < 13:
        print(i, "*", j, " : ", (j * i))
        j += 1
    print("-----------")
    j = 1
    i += 1