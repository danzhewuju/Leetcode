import collections
def run():
    n = int(input())
    data = collections.defaultdict(int)
    for i in range(n):
        id_, name = input().split()
        data[name] += 1
    res = 0
    for k, value in data.items():
        if value >= 2:
            res += 1
    print(res)
    return res

run()

