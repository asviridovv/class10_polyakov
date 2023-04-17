def isPrisme(a):
    k = 2
    while k+k <= n and n % k != 0:
        k += 1
    return(k+k > n)

