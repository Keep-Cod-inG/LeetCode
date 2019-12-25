from util.LinkedList import *


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def convert2list(List):
            l = []
            cur = List
            while cur:
                l.append(cur.val)
                cur = cur.next
            return l

        res_dummy = ListNode(None)
        cur = res_dummy
        l1_list = convert2list(l1)
        l2_list = convert2list(l2)
        l_long = l1_list if len(l1_list) >= len(l2_list) else l2_list
        l_short = l1_list if len(l1_list) < len(l2_list) else l2_list
        l_res = []
        r = 0
        for i in range(len(l_long)):
            if i < len(l_short):
                num_short = l_short[i]
            else:
                num_short = 0
            sum = num_short + l_long[i] + r
            r = sum // 10
            l_res.append(sum % 10)
        if r != 0:
            l_res.append(r)
        for num in l_res:
            cur.next = ListNode(num)
            cur = cur.next
        return res_dummy.next


if __name__ == '__main__':
    solution = Solution()
    l1 = LinkedList([2, 4, 3])
    l2 = LinkedList([5, 6, 4])
    PrintLinkedList(l1)
    PrintLinkedList(l2)
    PrintLinkedList(solution.addTwoNumbers(l1, l2))
