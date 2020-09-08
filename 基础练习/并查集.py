'''
利用并查集来进行图有没有环的检测
'''
class DIJ:
    def __init__(self, parent):
        self.parent = parent
        pass
    
    def find_root(self, x):
        '''
        寻找x的根节点
        '''
        root_x = x 
        while self.parent[root_x] != -1:
            root_x = self.parent[root_x]
        return root_x
    
    def union(self, x, y):
        root_x = self.find_root(x)
        root_y = self.find_root(y)
        if root_x == root_y: # 表示在一个集合内，无法合并
            return False
        else:
            self.parent[root_x] = root_y # root_x‘s parent is root_y
            return True


if __name__ == "__main__":
    graph = [[0, 1], [1, 2] , [6, 3], [4, 6], [0, 4], [4, 5]]
    parent = [-1]*7 # 初始化
    dij = DIJ(parent)
    for x, y in graph:
        if not dij.union(x, y):
            print("Cycle detected!")
            exit()
    print('No Cycle detected!')