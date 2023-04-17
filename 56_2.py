import random
A = [random.randint(0, 100) for b in range(10)]
B = []
print(*A)
def a(b):
    k = 2
    while k * k <= b and b % k != 0:
        k += 1
    return(k * k > b)
for b in A:
    if a(b) == True:
        B.append(b)
print("Массив B:\n",*B)
