import math
print("Введите координаты точки A:")
x1, y1 = map(float, input().split())
print("Введите координаты точки B:")
x2, y2 = map(float, input().split())
print("Длина отрезка AB = {:1.3f}".format(math.sqrt((x1-x2)**2+(y1-y2)**2)))s
