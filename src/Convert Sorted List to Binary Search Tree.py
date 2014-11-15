# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def find_mid(self, head):
        dummy = ListNode(-1)
        if head is None:
            return None
        dummy.next = head
        fast_p = head
        slow_p = head
        prev = dummy
        while fast_p is not None and fast_p.next is not None:
            prev = slow_p
            fast_p = fast_p.next.next
            slow_p = slow_p.next
        prev.next = None
        return slow_p

    def build_tree(self, head):
        if head is None:
            return None
        mid = self.find_mid(head)
        root = TreeNode(mid.val)
        if head == mid:
            root.left = None
        else:
            root.left = self.build_tree(head)
        root.right = self.build_tree(mid.next)
        return root

    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        return self.build_tree(head)
