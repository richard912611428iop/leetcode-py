# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        dummy_head = ListNode(0)
        dummy_head.next = head
        fast_node = dummy_head
        slow_node = dummy_head
        while n > 0:
            fast_node = fast_node.next
            n -= 1
        while fast_node is not None and fast_node.next is not None:
            fast_node = fast_node.next
            slow_node = slow_node.next
        slow_node.next = slow_node.next.next if (
            slow_node.next is not None) else None

        return dummy_head.next
