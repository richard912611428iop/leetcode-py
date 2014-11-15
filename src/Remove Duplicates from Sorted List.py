# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None:
            return None
        last_node = None
        p = head
        while p is not None:
            if last_node is None:
                last_node = p
                p = p.next
            else:
                if last_node.val != p.val:
                    last_node.next = p
                    last_node = p
                    p = p.next
                else:
                    p = p.next
        last_node.next = None
        return head
