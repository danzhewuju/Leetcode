def run(nums, target):
    res = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target:
                res += [nums[i], nums[j]]
                break
    return res


res = run([2, 7, 11, 15], 9)
print(res)