# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head.next:
            return None
        fast, slow = head, head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast and fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head