fileinput = open("inputn.txt", "r", encoding="utf8")
fileoutput = open("outputn.txt", "w", encoding="utf8")
n = fileinput.readlines()
A = []

for i in range(len(n)):
    A.append(n[i].split())
for i in A:
    if int(i[2]) > 80:
        fileoutput.write(f"{i[0]} {i[1]}\n")
fileinput.close()
fileoutput.close()