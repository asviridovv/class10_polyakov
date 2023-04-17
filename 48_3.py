def revs1(a):
    b = 0
    while a > 0:
        b = b*10+a%10
        a = a//10
    return(b)
a = int(input("Введите натуральное число: \n"))
b = revs1(a)
print("После переворота:", b, end=".")
