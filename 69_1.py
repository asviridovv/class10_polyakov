infile = open("sum1.txt", "r")
outfile = open("sum2.txt", "w")
b = infile.read().split()
n = list(map(int, b))

f1 = sum(n)/len(n)
print(f1)

outfile.write(str(f1))
outfile.close()
infile.close()