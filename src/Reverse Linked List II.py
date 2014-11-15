# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if head is None or m == n:
            return head
        dummy_node = ListNode(-1)
        dummy_node.next = head
        p_n_node = dummy_node
        p_m_node = dummy_node
        prev = dummy_node
        cur = dummy_node
        for i in range(m - 1):
            p_m_node = p_m_node.next
        p_n_node = p_m_node.next
        seg_tail = p_m_node.next
        cur = p_m_node.next
        prev = p_m_node
        next_node = cur.next
        for i in range(n - m + 1):
            p_n_node = p_n_node.next
            cur.next = prev
            prev = cur
            cur = next_node
            if cur is not None:
                next_node = cur.next
        seg_head = prev
        seg_tail.next = p_n_node
        p_m_node.next = seg_head

        return dummy_node.next
