class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def LinkedList(l):
    dummy = ListNode(None)
    pre = dummy
    for ele in l:
        pre.next = ListNode(ele)
        pre = pre.next
    return dummy.next

def PrintLinkedList(l):
    cur = l
    res_str = ""
    while cur:
        res_str += str(cur.val)
        if cur.next:
            res_str += " -> "
        cur = cur.next
    print(res_str)
