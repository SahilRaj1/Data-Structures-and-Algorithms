"""Power of a number using recursion"""

def power(n,exp):
    assert exp>=0 and int(exp)==exp, "The power should be a positive integer"
    if exp==1:
        return n
    else:
        return n*power(n,exp-1)


n, exp = map(int, input().split())
print(power(n,exp))
