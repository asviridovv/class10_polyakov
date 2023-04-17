from random import randint
a = randint(100, 999)
print("Получено число ", a, ".", sep="")
print("Его цифры {}, {}, {}".format(a//100, a//10%10, a%10), ".", sep="")