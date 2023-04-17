from random import randint
A = [randint(0, 10) for i in range(10)]
B = sorted(A)

print("Массив: \n", *A)
print("После сортировки: \n", *B)
