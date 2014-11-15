# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head = ListNode(-1)
        body = head
        p = l1
        q = l2
        while p is not None and q is not None:
            if p.val < q.val:
                body.next = p
                body = body.next
                p = p.next
            else:
                body.next = q
                body = body.next
                q = q.next
        while p is not None:
            body.next = p
            body = body.next
            p = p.next
        while q is not None:
            body.next = q
            body = body.next
            q = q.next
        return head.next
