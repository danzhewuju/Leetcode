class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        self.dic, self.po = {}, preorder
        for i in range(len(inorder)):
            self.dic[inorder[i]] = i
        return self.recur(0, 0, len(inorder)-1)
    
    def recur(self, pre_root, in_left, in_right):
        if in_left > in_right : return 
        root = TreeNode(self.po[pre_root])
        i = self.dic[self.po[pre_root]]
        root.left = self.recur(pre_root+1, in_left, i-1)
        root.right = self.recur(i-in_left+pre_root+1, i+1, in_right)
        return root

Sol = Solution()
root = Sol.buildTree([3,9,20,15,7], [9,3,15,20,7])
print(root)