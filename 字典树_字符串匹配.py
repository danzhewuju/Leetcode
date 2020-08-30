import collections
class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.idx = None

class TrieTree:
    def __init__(self):
        self.root = Node()
    def insert(self, word, x):
        node = self.root
        for w in word:
            node = node.children[w]
        # if node:
        node.idx = x

class Solution:
    def multiSearch(self, big, smalls):
        # create trietree
        trie = TrieTree()
        for i, word in enumerate(smalls):
            trie.insert(word, i)
        
        res = [[] for _ in range(len(smalls))]
        
        for i in range(len(big)):
            node = trie.root
            if big[i] not in node.children.keys():
                continue
            for j in range(i, len(big)):
                node = node.children[big[j]]
                # print(node.children)
                if node.idx != None:
                    res[node.idx].append(i)
                    
                
        return res
            

Sol = Solution()
print(Sol.multiSearch("mississippi", ["is","ppi","hi","sis","i","ssippi"]))