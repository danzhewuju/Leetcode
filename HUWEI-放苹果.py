# 回溯的方法来做
def run():
    M , N = [int(x) for x in input().split()]
    res = set()
    def helper(nums:list):
        if sum(nums) > M or len(nums) > N:
            return 
        if len(nums) <=  N and sum(nums) == M:
            
            if len(nums) < N: nums += [0]*(N-len(nums))
            nums.sort()
            tmp = tuple(nums)
            if tmp not in res:
                res.add(tmp)
            return
        for i in range(M+1):
            helper(nums+[i])
    helper([])
    return len(res)

print(run())
