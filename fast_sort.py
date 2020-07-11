import random
import time

nums = [random.randint(0, 10000) for _ in range(1000)]
nums_1 = nums.copy()
nums_2 = nums.copy()
# print(nums)


def fast_sort(left, right):
    if left > right:
        return
    sign = nums[left]
    p1, p2 = left, right
    while p2 > p1:
        while p2 > p1 and nums[p2] >= sign:  # 右侧找到第一个小于标准的数
            p2 -= 1
        nums[p1] = nums[p2]
        while p2 > p1 and nums[p1] < sign:
            p1 += 1
        nums[p2] = nums[p1]
    nums[p1] = sign
    fast_sort(left, p1 - 1)
    fast_sort(p1 + 1, right)


def select_sort():
    for i in range(len(nums_2)):
        for j in range(len(nums_2) - i - 1):
            if nums_2[j + 1] < nums_2[j]:
                tmp = nums_2[j]
                nums_2[j] = nums_2[j + 1]
                nums_2[j + 1] = tmp

print("1.快排")
start = time.time()
# print(nums)
fast_sort(0, len(nums) - 1)
# print(nums)
end = time.time()
print(end - start)
print("2.python 内置函数")
start = time.time()
# print(nums_1)
nums_1.sort()
# print(nums_1)
end = time.time()
print(end - start)
print("3.冒泡排序")
start = time.time()
# print(nums_2)
select_sort()
# print(nums_2)
end = time.time()
print(end - start)
