class Solution:
    def pre_order(self, idx):
        if idx < 0 or idx >= len(self.input):
            return
        if self.input[idx] != -1:
            self.tmp.append(self.input[idx])
            self.pre_order(idx*2+1)
            self.pre_order(idx*2+2)

    def in_order(self, idx):
        if idx < 0 or idx >= len(self.input):
            return
        if self.input[idx] != -1:
            self.in_order(idx*2+1)
            self.tmp.append(self.input[idx])
            self.in_order(idx*2+2)

    def back_order(self, idx):
        if idx < 0 or idx >= len(self.input):
            return
        if self.input[idx] != -1:
            self.back_order(idx*2+1)
            self.back_order(idx*2+2)
            self.tmp.append(self.input[idx])

    def binaryTreeScan(self, input_):
        # write code here
        self.input = input_
        self.res = []
        self.tmp = []

        self.pre_order(0)
        tmp = self.tmp.copy()
        self.res.append(tmp)
        self.tmp.clear()
        self.in_order(0)
        tmp = self.tmp.copy()
        self.res.append(tmp)
        self.tmp.clear()
        self.back_order(0)
        tmp = self.tmp.copy()
        self.res.append(tmp)
        self.tmp.clear()
        return self.res

Sol = Solution()
res = Sol.binaryTreeScan([1,7,2,6,-1,4,8])
print(res)
