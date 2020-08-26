def tran_int_bit(n):  # 将整数转化为二进制的整数数组
    res = bin(n)
    res = res[2:]
    return list(res)


def trans_bit_int(data):
    str_a = ''.join(data)
    # print(str_a)
    res = int(str_a, 2)
    return res


def highest_bit(data):  # 给个一维数组给你求最高位的序号
    i = 0
    while data[i] == '0':  # [0,0,0, 1, 1, 1] index = 3
        i += 1
    return i


def run():
    d = [int(x) for x in input().split()]
    n = len(d)
    info = []
    for x in d:
        tmp = tran_int_bit(x)
        info.append(tmp)  # 构建为二维矩阵

    # 换位操作
    for i in range(n):
        if len(info[i]) % 2 == 1:
            info[i] = ['0'] + info[i]
        j = len(info[i]) - 1
        while j - 1 > -1:
            info[i][j], info[i][j-1] = info[i][j-1], info[i][j]  # 交换
            j -= 2
    # 移位的操作
    last = info[0][-2:]
    for i in range(1, n):
        new_last = info[i][-2:]
        tmp = info[i][:-2]
        info[i] = last + ['0']*(32-len(tmp)-2)+tmp
        last = new_last

    tmp = info[0][:-2]
    info[0] = last + ['0']*(32-len(tmp)-2)+tmp
    for i in range(n):
        if i != n-1:
            print(trans_bit_int(info[i]), end=' ')
        else:
            print(trans_bit_int(info[i]), end='')
    return


if __name__ == "__main__":
    run()
    # print(trans_bit_int(['1', '0', '1', '1', '1', '0']))

    pass
