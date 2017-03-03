# Given a singly linked list, determine if it is a palindrome.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Runtime Error
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        temp = head
        i = 0
        # 求链表的长度
        while temp:
            temp = temp.next
            i += 1
        # 中间位置 + 1
        fix = i / 2 + 1 if i % 2 != 0 else i / 2
        pos = 0
        tail = head
        pre = []
        # 将中间以前的值加入到pre中
        while pos < fix:
            pre.append(tail.val)
            tail = tail.next
            pos += 1
        beh = []
        # 将中间以后的值加入到beh中
        while tail:
            beh = [tail.val] + beh
            tail = tail.next
        return pre == beh or pre[:len(pre)-1] == beh

    def isPalindrome1(self, head):
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        # compare the first and second half nodes
        while node:  # while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True

