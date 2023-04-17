fileinput = open("inputn.txt", "r", encoding="utf8")
fileoutput = open("outputc.txt", "w", encoding="utf8")
n = fileinput.readlines()
A = []

for i in range(len(n)):
    A.append(n[i].split())
count = 0

for i in A:
    if int(i[2]) > 80:
        count += 1
        fileoutput.write(f"{count}) {i[1][0]}. {i[0]}\n")