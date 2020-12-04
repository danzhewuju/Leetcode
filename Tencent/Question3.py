class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def create_link():
    nums1 = [int(x) for x in input().split()]
    nums2 = [int(x) for x in input().split()]
    head1, head2 = None, None
    cur1, cur2 = head1, head2
    while nums1:
        p = Node(nums1.pop(0))
        if not head1:
            head1 = p
            cur1 = head1
        else:
            cur1.next = p
            cur1 = p
    while nums2:
        p = Node(nums2.pop(0))
        if not head2:
            head2 = p
            cur2 = head2
        else:
            cur2.next = p
            cur2 = p

    return head1, head2

def read_link(head):
    res = []
    if not head:
        print('0')
        return
    while head:
        res.append(str(head.val))
        head = head.next
    print("".join(res))
    return 

def reversed(head):
    pre, p = None, head
    while p:
        tmp = p.next
        p.next = pre
        pre = p
        p = tmp
    return pre

def run():
    head1, head2 = create_link()
    read_link(head1)
    read_link(head2)
    head1_r, head2_r = reversed(head1), reversed(head2)
    p1, p2 = head1_r, head2_r
    new_head = None
    cur = None
    bit_p = 0   # 是否为负位
    while p1 and p2:
        tmp = p1.val-p2.val-bit_p
        bit_p = 0
        if tmp < 0:
            tmp += 10
            bit_p = 1
        new_p = Node(tmp)
        if not new_head:
            new_head = new_p
            cur = new_p
        else:
            cur.next = new_p
            cur = new_p
        p1 = p1.next
        p2 = p2.next
    
    while p1:
        tmp = p1.val-bit_p
        bit_p = 0
        if tmp < 0:
            tmp += 10
            bit_p = 1
        new_p = Node(tmp)
        cur.next = new_p
        cur = new_p
        p1 = p1.next
    while p2:
        tmp = p2.val-bit_p
        bit_p = 0
        if tmp < 0:
            tmp += 10
            bit_p = 1
        new_p = Node(tmp)
        cur.next = new_p
        cur = new_p
        p2 = p2.next
    new_head = reversed(new_head)
    # while new_head and new_head.val == 0:
    #     new_head = new_head.next
    read_link(new_head)

    return new_head


run()