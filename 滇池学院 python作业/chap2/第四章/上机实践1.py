def jinzita(n):
    p = int((n + 1) / 2)
    for i in range(1, p + 1, 1):
        for j in range(p - i):
            print(" ", end = "")
        for k in range(2 * i - 1):
            print("*",end = "")
        for q in range(p - i):
            print(" ", end = "")
        print()

print(jinzita(n = eval(input())))


