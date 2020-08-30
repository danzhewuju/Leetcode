import collections


class Node:
    def __init__(self):

        self.children = collections.defaultdict(Node)
        self.isWord = False


class TrieTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True


class Solution:
    def findWords(self, board, words):
        m, n = len(board), len(board[0])
        res = []
        trie = TrieTree()
        node = trie.root
        for word in words:
            trie.insert(word)
        for i in range(m):
            for j in range(n):
                self.dfs(board, node, "", i, j, res)
        return res

    def dfs(self, board, node, path, i, j, res):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if node.isWord:
            res.append(path)
            node.isWord = False # 不设置的话，由于程序会继续扩展的搜索，会发生重复的情况。
        tmp = board[i][j]
        node = node.children.get(tmp, None)
        if not node:
            return
        board[i][j] = '#'  # 修改访问的标识，避免重复的访问
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            self.dfs(board, node, path+tmp, i+dx, j+dy, res)
        board[i][j] = tmp


Sol = Solution()
words = ["oath", "pea", "eat", "rain"]
board = [
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']]
print(Sol.findWords(board, words))
