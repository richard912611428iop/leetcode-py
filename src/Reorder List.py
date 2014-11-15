# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def rerverse_list(self, head):
        if head is None:
            return None
        prev = None
        p = head
        p_next = head.next
        while p is not None:
            p_next = p.next
            p.next = prev
            prev = p
            p = p_next
        return prev

    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head is None:
            return
        fast_p = head
        slow_p = head
        while fast_p is not None and fast_p.next is not None:
            fast_p = fast_p.next.next
            slow_p = slow_p.next
        rest_half = slow_p.next
        slow_p.next = None
        rest_half = self.rerverse_list(rest_half)
        p = head
        q = rest_half
        while p is not None and q is not None:
            p_next = p.next
            q_next = q.next
            p.next = q
            q.next = p_next
            p = p_next
            q = q_next
        return
