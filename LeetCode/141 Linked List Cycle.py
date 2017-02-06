# Given a linked list, determine if it has a cycle in it.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # 超时
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        curr, sofar = head, head
        while sofar:
            if sofar.next == curr:
                return True
            sofar = sofar.next
        return self.hasCycle(head.next)

    def hasCycle1(self, head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False


