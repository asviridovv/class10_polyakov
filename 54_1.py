from random import randint
i = randint(1, 20)
A, n = [0]*i, 0
for n in range(0, i, 1):
    A[n] = randint(0, 20)
print("Массив: \n", *A)
print("Минимальный элемент: A[", A.index(min(A)), "]=", min(A), sep="")
print("Максимальный элемент: A[", A.index(max(A)), "]=", max(A), sep="")