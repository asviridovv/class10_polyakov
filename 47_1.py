def num (a, b, c):
    if a > b > c:
        print (c, b, a)
    elif b > a > c:
        print(c, a, b)
    elif c > a > b:
        print(b, a, c)

print("Введите три целых числа:")
a, b, c = map(int, input().split())
num