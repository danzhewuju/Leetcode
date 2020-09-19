import math
def isprim(n):
    d = int(math.sqrt(n))+1
    for i in range(2, d):
        if n % i == 0:
            return False
    return True

def run():
    n = 24
    first = n
    i = 2
    res = []
    while n > 1:
        while n % i == 0:
            res.append(str(i))
            n //= i
        i += 1
    res = "*".join(res)
    res += "="+ str(first)
    print(res)
    return res

run()

