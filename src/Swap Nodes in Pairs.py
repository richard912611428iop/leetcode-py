# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def swap_node(self, n1, n2, n3, n4):
        if n3 is None and n4 is None:
            return
        n1.next = n3
        n3.next = n2
        n2.next = n4
        return

    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        dump_node = ListNode(-1)
        p = dump_node
        p.next = head
        while p is not None:
            n1 = p
            n2 = p.next
            n3 = n2.next if n2 is not None else None
            n4 = n3.next if n3 is not None else None
            self.swap_node(n1, n2, n3, n4)
            p = p.next.next if p.next is not None else None
        return dump_node.next
