'''
题目描述：
牛牛有一个n个数字的序列，现在牛牛想把这个序列分成k段连续段，牛牛想知道分出来的k个连续段的段内数字和的最小值最大可以是多少
'''
def run():
    '''
    每一段的最小的值的最大值
    '''
    s, k, a = int(input()), int(input()), [int(x) for x in input().split()]
    res = []
    # 利用回溯的方法来实现
    x, y = 0, sum(a)
    if k == 1: return y
    while y -x > 1:
        mid = (x+y)/2
        segment, nowval = 0, 0
        for i in range(s):
            nowval += a[i]
            if nowval >= mid:
                segment += 1
                nowval = 0
        if segment >= k:
            x = mid
        else:
            y = mid
    return round((x+y)/2) 


if __name__ == "__main__":
    # print(run())
    print(round(1.4999999999999))
