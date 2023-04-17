filein = open("input2.txt", "r")
fileout = open("output2.txt", "w")
n = filein.read().split()
A = list(map(int, n))
B = []

for i in range(len(A)):
    if A[i] % 2 == 0:
        B.append(A[i])

if (min(B) == max(B)):
    fileout.write("None")
else:
    fileout.write(str(min(B))+"\n")
    fileout.write(str(max(B)))
fileout.close()
filein.close()