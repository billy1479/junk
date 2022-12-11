def modulus(m ,n):
    """returns value of m mod n"""
    if (m - n) <= 0:
        return m
    else:
        return modulus((m - n), n)

print('Numbers are in the format M % N = OUTPUT')
m = int(input('Please enter in m: '))
n = int(input('Please enter in n: '))
print(modulus(m, n))