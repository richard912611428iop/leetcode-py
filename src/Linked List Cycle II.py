# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None
        slow = head.next
        fast = head.next.next

        while fast is not None and fast.next is not None and fast != slow:
            slow = slow.next
            fast = fast.next.next
        if fast is None or fast.next is None:
            return None

        fast = head

        while fast != slow:
            fast = fast.next
            slow = slow.next

        return fast
