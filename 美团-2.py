def run():
    n = int(input()) # 购买票的次数
    info = [[""]*2 for _ in range(n)] # 使用二维列表存储出发地-目的地
    for i in range(n):
        start, end = input().split()
        info[i][0], info[i][1] = start, end
    
    # 考虑到字符匹配的过程 利用栈做一个匹配, 需要考虑到大环镶嵌小环
    stack = []
    ans = 0
    for i in range(len(info)):
        start, end = info[i][0], info[i][1]
        stack.append(start)
        if end in stack: # 查询到一个有一个目的地和出发地重合
            index = stack.index(end) # 找到这个出发地索引，索引之后的数据全部弹出
            stack = stack[:index]
            ans += 1
    return ans

print(run())
            

