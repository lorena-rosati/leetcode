# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # without the use of a stack

        fast, slow = head, head
        while fast:
            fast = fast.next
            if fast:
                fast, slow = fast.next, slow.next
        return slow

