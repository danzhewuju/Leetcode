def list_num(n):
    last = 0
    while n > 0:
        tmp = n % 10
        if tmp < last:
            return False
        else:
            last = tmp
            n //= 10
    return True


def minnum():
    n = int(input())
    if n <= 10:
        print(n)
        return

    while True:
        if list_num(n):
            break
        else:
            n += 1
    print(n)
    return

minnum()
