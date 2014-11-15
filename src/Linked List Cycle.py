# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        fast_p = head
        slow_p = head
        while fast_p is not None and fast_p.next is not None:
            fast_p = fast_p.next.next
            slow_p = slow_p.next
            if fast_p == slow_p:
                return True
        return False
