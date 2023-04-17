from random import randint
i = randint(1, 10)
A, n = [0]*i, 0
for n in range(0, i, 1):
    A[n] = randint(0,5)

print("Массив: \n", *A, "\nЧто ищем:")
x = int(input())
print("Нашли: ")

n = 0
for n in range(0, i, 1):
    if A[n] == x:
        print(f"A[{n}]={x}, ".format(), end="")