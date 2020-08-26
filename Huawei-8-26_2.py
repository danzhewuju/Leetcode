def run():
    line = input()
    tmp_1, tmp_2 = line.split('],[')
    tmp_1 = tmp_1[1:]
    tmp_1.strip()
    tmp_2.strip()
    tmp_2 = tmp_2[1:]
    w = [int(x) for x in tmp_1.split(',')]  # 箱子的宽度
    h = [int(x) for x in tmp_2.split(',')] # 箱子的高度
    n = len(w)       # 箱子的个数
    res = 0 # 初始化矩形的面积
    for i in range(n):
        for j in range(i+1, n+1):
            new_area = sum(w[i:j])*min(h[i:j])  # 计算面积
            res = max(res, new_area)
    print(res)
    return res


if __name__ == "__main__":
    run()