# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        great_head = ListNode(-1)
        less_head = ListNode(-1)
        prev = great_head
        p = head
        p_next = None
        q = less_head
        while p is not None:
            p_next = p.next
            if p.val < x:
                p.next = None
                q.next = p
                q = q.next
            else:
                prev.next = p
                prev = prev.next
            p = p_next
        prev.next = None
        q.next = great_head.next
        return less_head.next
