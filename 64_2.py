fname = input("Введите имя файла: ")
frash = input("Введите новое расширение: ")

if '.' not in fname:
    print(fname + "." + frash)

else:
    n = -1
    while fname[n] != ".":
        fname = fname[0:n]
    print(fname + frash)
