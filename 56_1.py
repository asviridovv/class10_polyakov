from random import randint
a = [randint(-10, 10) for x in range(20)]
n1 = [i for i in a if i<0 and i % 2 == 0]
print("Массив A: \n", *a)
print("Массив B: \n", *n1)