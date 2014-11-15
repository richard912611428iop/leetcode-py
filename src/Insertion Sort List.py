# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x


class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        vir_point = ListNode(1)
        vir_point.next = head
        if head is None:
            return None
        p = head.next
        head.next = None
        q = vir_point
        while p is not None:
            now = p
            p = p.next
            if now.val >= q.val:
                q = q
            else:
                q = vir_point
            while q.next is not None and now.val >= q.next.val:
                q = q.next
            now.next = q.next
            q.next = now
        return vir_point.next
