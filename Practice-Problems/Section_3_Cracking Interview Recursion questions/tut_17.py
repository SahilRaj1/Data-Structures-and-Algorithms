"""Sum of digits of a number"""

def sum_digits(n):
    assert n>=0 and int(n)==n, "The number must be a positive integer"
    if n == 0:
        return 0
    else:
        return n%10 + sum_digits(n//10)
    
n=int(input())
print(sum_digits(n))
