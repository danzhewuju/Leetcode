import numpy as np
import matplotlib.pyplot as plt


def getCentroids(clusterDict):
    # 得到k个质心
    centroidList = []
    for key in clusterDict.keys():
        centroid = np.mean(clusterDict[key], axis=0)  # 计算每列的均值，即找到质心
        centroidList.append(centroid)
    return np.array(centroidList).tolist()


def getVar(clusterDict, centroidList):
    # 计算簇集合间的均方误差
    # 将簇类中各个向量与质心的距离进行累加求和
    sum = 0.0
    for key in clusterDict.keys():
        vec1 = centroidList[key]
        distance = 0.0
        for item in clusterDict[key]:
            vec2 = item
            distance += calcuDistance(vec1, vec2)
        sum += distance
    return sum


def calcuDistance(vec1, vec2):
    return np.sqrt(np.sum(np.square(vec1 - vec2)))


def MinDistance(dataSet, centroidList):
    clusterDict = {}
    for i in range(len(dataSet)):
        flag = 0
        min_dis = float("inf")
        for j in range(len(centroidList)):
            distance = calcuDistance(dataSet[i], centroidList[j])
            if min_dis > distance:
                flag = j
                min_dis = distance
        if flag not in clusterDict.keys():
            clusterDict[flag] = list()
        clusterDict[flag].append(dataSet[i])
    return clusterDict


def showCluster(centroidList, clusterDict):
    # 展示聚类结果
    colorMark = ['or', 'ob', 'og', 'ok', 'oy', 'ow']  # 不同簇类的标记 'or' --> 'o'代表圆，'r'代表red，'b':blue
    centroidMark = ['dr', 'db', 'dg', 'dk', 'dy', 'dw']  # 质心标记 同上'd'代表棱形
    for key in clusterDict.keys():
        plt.plot(centroidList[key][0], centroidList[key][1], centroidMark[key], markersize=10)  # 画质心点
        for item in clusterDict[key]:
            plt.plot(item[0], item[1], colorMark[key])  # 画簇类下的点
    plt.show()


if __name__ == '__main__':
    k = 2  # 聚类种数
    dataSet = 10 * np.random.random((10, 2))
    centroidList = 10 * np.random.random((k, 2))
    clusterDict = MinDistance(dataSet, centroidList)
    newVar = getVar(clusterDict, centroidList)

    oldVar = -1  # 旧均方误差值初始化为-1
    showCluster(centroidList, clusterDict)  # 展示聚类结果
    k = 2
    while abs(newVar - oldVar) >= 0.000001:  # 当连续两次聚类结果小于0.0001时，迭代结束
        centroidList = getCentroids(clusterDict)  # 获得新的质心
        clusterDict = MinDistance(dataSet, centroidList)  # 新的聚类结果
        oldVar = newVar
        newVar = getVar(clusterDict, centroidList)
        print('***** 第%d次迭代 *****' % k)
        print('簇类')
        for key in clusterDict.keys():
            print(key, ' --> ', clusterDict[key])
        print('k个均值向量: ', centroidList)
        print('平均均方误差: ', newVar)
        k += 1
    showCluster(centroidList, clusterDict)  # 展示聚类结果