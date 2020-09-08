import numpy as np
def run():
    print("请输入病人的个数:")
    n = int(input())
    data = [[0]*5 for _ in range(n)]
    std = [[0]*5 for _ in range(n)]
    for i in range(n):
        for j in range(5):
            d, s = [float(x) for x in input().split()]
            data[i][j] = d
            std[i][j] = s
    avg = np.mean(np.array(data), axis=0)
    avg = [round(x, 4) for x in avg]
    avg_std = np.mean(np.array(std), axis=0)
    avg_std = [round(x, 4) for x in avg_std]
    print("性能:",avg)
    print("标准差", avg_std)
    print("&", end=' ')
    for i in range(5):
        print("{:.4f}±{:.4f}".format(avg[i], avg_std[i]),end=' & ')

while True:
    run()
    


