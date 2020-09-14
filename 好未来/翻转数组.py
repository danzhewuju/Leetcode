class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 向右翻转列表
# @param head ListNode类 listnode 中的头元素
# @param k int整型 向右翻转次数
# @return ListNode类
#
class Solution:
    def rotateRight(self , head , k ):
        # write code here
        nums = []
        p = head
        while p:
            nums.append(p.val)
            p = p.next
        new_list = nums[-k:] + nums[:-k]
        new_head = ListNode(nums[0])
        last = new_head
        for d in nums[1:]:
            tmp = ListNode(d)
            last.next = tmp
            last = tmp
        return new_head
