print("Выпало очков: ")
from random import randint
a, b, c = randint(1, 5), randint(1, 5), randint(1, 5)
print(a, b, c)
print("({:d}+{:d}+{:d})/3={:d}".format(a, b, c, (a+b+c)//3))