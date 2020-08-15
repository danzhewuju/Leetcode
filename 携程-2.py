class Tree:
    def __init__(self, name):
        self.name = name
        self.val = 0
        self.next = [] # 树的子节点
    def set_node(self, node_list):
        self.next = node_list
    def set_val(self, x):
        self.val = x

def create_tree(str_data): # 递归的方法构造树 str_data = 'HEAD`0`A,B,C
    # str_data 有三种类型 1. 带有'Head' 2. 带有END 3. 两者都没有
    # 将数据处理成字典的形式，再来构造树
    dict_info = {}  # 字典的格式{A:[next_node:[A, B, C], isEnd = True, val = 10]  # 
    data_info = str_data.split('|')
    for str_ in data_info:
        data_split = str_.split('`')
        node = data_split[0] # 当前节点信息
        node_str = data_split[-1] # 获取后面的节点信息 A,B,C 或者为END
        node_list = []
        isEnd = False
        if node_str == 'END':
            isEnd = True  # 此时是叶子节点
        else:
            node_list = node_str.split(',') # 改节点的子节点的列表
        val = int(data_split[1])
        info = {'next_node':node_list, 'isEnd':isEnd, 'val':val}
        dict_info[node] = info
    stack = []
    hashnode = {} # 需要构建hash表，来存储节点地址
    for node_name, info in dict_info.items():
        if node_name == 'HEAD':
            root = Tree(node_name)
            root.set_val(info['val'])
            hashnode[node_name] = root
            node_list = [Tree(x) for x in info['next_node']]
            root.set_node(node_list)
            for p in node_list:
                hashnode[p.name] = p
        else:
            hashnode[node_name].set_val(info['val'])
            if info['isEnd'] != True:
                node_list = [Tree(x) for x in info['next_node']]
                for p in node_list:
                    hashnode[p.name] = p
                hashnode[node_name].set_node(node_list)
    return hashnode['HEAD']

def run():
    data = "HEAD`0`A,B,C|A`20`END|B`100`END|C`50`D,E|D`80`F|E`150`END|F`30`END"
    # str_data 有三种类型 1. 带有'Head' 2. 带有END 3. 两者都没有
    root = create_tree(data)
    res = 0
    def dfs(node, sum_):
        nonlocal res
        if not node.next:
            res = max(res, sum_)
            return 
        for p in node.next:
            dfs(p, sum_ + p.val)
    dfs(root, 0)
    return res



print(run())
    



