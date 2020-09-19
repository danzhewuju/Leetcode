class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
def init():
    p1 = [1, 2, 3, 7]
    p2 = [2, 4, 5, 9]
    head1 = Node(p1[0])
    p = head1
    for d in p1[1:]:
        node = Node(d)
        p.next = node
        p = p.next
    head2 = Node(p2[0])
    p = head2
    for d in p2[1:]:
        node = Node(d)
        p.next = node
        p = p.next
    return head1, head2

def read(head):
    p = head
    while p:
        print(p.val, end = ' ')
        p = p.next
    print('\n')
    return 

def run():
    head1, head2 = init()
    read(head1)
    read(head2)
    p1, p2 = head1, head2
    if p1.val <= p2.val:
        new_head = p1
        p1 = p1.next
    else:
        new_head = p2
        p2 = p2.next
    last = new_head
    while p1 and p2:
        if p1.val <=  p2.val:
            last.next = p1
            last = p1
            p1 = p1.next
        else:
            last.next = p2
            last = p2
            p2 = p2.next
    if p1:
        last.next = p1
    if p2:
        last.next = p2
    return new_head

p = run()
while p:
    print(p.val,end = ' ')
    p = p.next



         




