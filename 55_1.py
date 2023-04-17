import random
A = [random.randint(0,5) for i in range(6)]
print("Массив: \n", *A)
c = A[0]
for n in range(len(A)-1):
    A[n] = A[n+1]
A[len(A)-1] = c
print("Результат:\n", *A)