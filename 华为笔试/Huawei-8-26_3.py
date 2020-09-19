def all_cases(str_a, m, n):
    '''
    对于字符串, str_a, 其中m个正确的位置以及n个存在但是位置不正确的所有情况
    '''
    res = [] # 存储所有的情况
    def dfs(idx, index_list): #利用深度搜索来确定全排列的位置信息
        if len(index_list) == m:
            res.append(index_list)
            return 
        if idx >= len(str_a):
            return 
        for i in range(idx, len(str_a)):
            dfs(i+1, index_list+[i])  # 构成新的递归条件
    dfs(0, [])
    

def run():
    N = int(input()) # 单词的长度
    T = int(input()) # 猜测的次数
    info = []
    for i in range(T):
        info.append([int(x) for x in input().split()])  # 作为数据的输入
    # 需要构造一个递归的方法
    
    
    

if __name__ == "__main__":
    run()
    pass