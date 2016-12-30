# Reverse a singly linked list.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        nextNode = head.next
        newHead = self.reverseList(nextNode)
        nextNode.next = head
        head.next = None
        return newHead
