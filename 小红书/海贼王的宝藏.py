def list_unit(nums, index):  # 合并列表
    res = []
    count = 0
    if index + 1 < len(nums) and nums[index+1] < 0:
        if nums[index] + nums[index + 1] >= 0:
            nums[index] = nums[index]+nums[index+1]
            nums[index+1] = 0
            count += 1
    if 0 <= index - 1 and nums[index-1] < 0:
        if nums[index] + nums[index-1] >= 0:
            nums[index] = nums[index-1] + nums[index]
            nums[index-1] = 0
            count += 1
    res = [x for x in nums if x != 0]
    return res, count


def run():
    N = int(input())
    A = [int(x) for x in input().split()]
    avg = sum(A) // N
    res = 0
    B = [x-avg for x in A]  # 每一个位置所缺的硬币数
    B = [x for x in B if x != 0]
    while B:
        tmp_index = 0
        for index, x in enumerate(B):
            if x > 0:
                tmp_index = index
                break
        B, d = list_unit(B, tmp_index)
        res += d
    print(res)
    return


run()
