# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 
# @param head ListNode类 
# @return ListNode类
#
class Solution:
    def reversedList(self, head):
        cur, p = None, head
        while p:
            tmp = p.next
            p.next = cur
            cur = p
            p = tmp
        return cur
    
    def mergeList(self,headA, headB):
        p, q = headA, headB
        new_head = headA
        while p and q:
            tmp = q.next
            q.next = p.next
            p.next = q
            p = p.next.next
            q = tmp
        return new_head
        
    def reorderList(self , head ):
        # write code here
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        next_node = slow.next
        slow.next = None
        mid = self.reversedList(next_node)
        new_head = self.mergeList(head, mid)
        return new_head
        