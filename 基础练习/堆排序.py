class Solution:
    def countSmaller(self, nums):
        def bi_search(num_list, k): 
            n = len(num_list) 
            if n == 0:
                return 0
            l, r = 0, n-1
            while r > l:
                mid = (r+l) // 2
                if num_list[mid] == k:
                    l = mid
                    break
                elif num_list[mid] > k:
                    r = mid -1 
                else:
                    l = mid + 1
            return l + 1 if num_list[l] < k else l  # 返回的是其所在的id序号
        
        res, nums_tmp,n = [], [], len(nums)
        for i in range(n-1, -1, -1):
            m = nums[i]
            idx = bi_search(nums_tmp, m)
            nums_tmp.insert(idx, m)
            res.append(idx)
        return res[::-1]

solu = Solution()
print(solu.countSmaller([5,2,6,1]))