"""Decimal to binary"""


def decimalToBinary(n):
    assert int(n) == n, "The number must be be an integer"
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimalToBinary(n // 2)


n = int(input())
print(decimalToBinary(n))
