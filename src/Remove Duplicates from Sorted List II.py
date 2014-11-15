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
        if head.next is None:
            return head
        result = ListNode(0)
        p = head
        q = result
        flag = True
        while p.next is not None:
            if p.val != p.next.val:
                if flag:
                    q.next = ListNode(p.val)
                    q = q.next
                    p = p.next
                else:
                    flag = True
                    p = p.next
            else:
                flag = False
                p = p.next

        if flag:
            q.next = ListNode(p.val)
        result = result.next

        return result
