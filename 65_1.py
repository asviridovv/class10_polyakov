def TumbaYumba (a, w, k):
    if len(w) == k - 1:
        print(w[0], a[0], w[1:])
        return
    else:
        for i in a:
            TumbaYumba(a, w+i, k)
k = int(input("Введите количество букв в слове: "))
TumbaYumba("ЫШЧО", "", k)
