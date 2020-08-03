class Solution:
    def smallestRange(self, nums):
        point = [0]*len(nums) # 指针的列表
        data = [0]*len(nums)
        for i in range(len(nums)):
            data[i] = nums[i][point[i]]
        min_, max_ = min(data), max(data)

        while True:
            minp = 0
            cur_min_, cur_max_ =  min(data), max(data)
            if cur_max_-cur_min_ < max_ - min_:
                max_= cur_max_
                min_ = cur_min_
            index = data.index(cur_min_)
            if point[index] < len(nums[index])-1:
                point[index] += 1
                data[index] = nums[index][point[index]]
            else:
                break
        return [min_, max_]