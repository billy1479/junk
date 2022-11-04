def modulus(m ,n):
    """returns value of m mod n"""
    if (m - n) <= 0:
        return m
    else:
        return modulus((m - n), n)

print(modulus(30,7))