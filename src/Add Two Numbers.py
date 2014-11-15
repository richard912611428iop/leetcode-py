# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(-1)
        carry = 0
        prev = dummy
        pa = l1
        pb = l2
        while pa is not None or pb is not None:
            ai = 0 if pa is None else pa.val
            bi = 0 if pb is None else pb.val
            value = (ai + bi + carry) % 10
            carry = (ai + bi + carry) // 10
            prev.next = ListNode(value)
            pa = None if pa is None else pa.next
            pb = None if pb is None else pb.next
            prev = prev.next
        if carry > 0:
            prev.next = ListNode(carry)
        return dummy.next
