def logf(a):
    b = a//2
    c = 0

    for i in range(1, b+1):
        if a % i == 0:
            c += i

    if a == c:
        return True
    else:
        return False

a = int(input("Введите натуральное число: \n"))
if logf(a):
    print("Число", a, "совершенное", end = ".")
else:
    print("Число", a, "не совершенное", end = ".")
