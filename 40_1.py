print("Введите три целых числа:")
a, b, c = map(int, input().split())

print(a, "+", b, "+", c, "=", a+b+c, sep="")
print(a, "*", b, "*", c, "=", a*b*c, sep="")
print("({:d}+{:d}+{:d})/3={:1.3f}".format(a,b,c,(a+b+c)/3))