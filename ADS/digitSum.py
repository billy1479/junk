# Takes an integer as input and sums the subintegers within and outputs it i.e. 123 would output 6
def DigitSum(n):
    if n == 0:
        return 0
    else:
        return int(n % 10) + int(DigitSum(int(n / 10)))
