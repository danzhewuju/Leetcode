# 根据前序遍历和后序遍历来构建二叉树
class Tree:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
# 根据前序遍历和中序遍历来构造二叉树
def CreateTree(pre_order, mid_order):
    if not pre_order:
        return None
    else:
        root = Tree(pre_order[0])
        index = mid_order.index(pre_order[0])
        left = CreateTree(pre_order[1:index+1], mid_order[:index])
        right = CreateTree(pre_order[index+1:], mid_order[index+1:])
        root.left,root.right = left, right
        return root

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val, end=' ')
    inorder(root.right)


def preorder(root):
    if not root:
        return
    print(root.val, end=' ')
    preorder(root.left)
    preorder(root.right)


def run():
    pre_order = [1, 2, 4, 5, 3, 6, 7]
    mid_order = [4, 2, 5, 1, 6, 3, 7]
    root = CreateTree(pre_order, mid_order)
    preorder(root)
    print('\n')
    inorder(root)

run()

        
    
    