def logf2(a, b):
    while b > 0:
        a, b = b, a%b
    if a == 1:
        return True
    else:
        return False

a, b = map(int, input("Введите два натуральных числа: \n").split())
if logf2(a, b):
    print(f"Числа {a} и {b} взаимно простые", end = ".")
else:
    print(f"Числа {a} и {b} не взаимно простые", end = ".")