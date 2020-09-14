import collections
def run():
    n = int(input())
    a = [int(x) for x in input().split()]
    a = collections.Counter(a)
    a = sorted(a.items(), key=lambda x: -x[1])
    print(a[0][1])
    return  
    # 直接求众数
    

run()