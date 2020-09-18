res = []
A = [1, 2, 3, 4 ,5, 6]
n = len(A)
d = 7
n = 2
def dfs(idx, nums,sum_a, A, d):
    if len(nums) == n and sum_a == d:
      res.append(nums)
      return
    if len(nums) > n or sum_a > d:
      return 
    for i in range(idx, len(A)):
        dfs(i+1, nums+[A[i]], sum_a+A[i], A, d)
    return 

dfs(0, [], 0, A, d)
print(res)