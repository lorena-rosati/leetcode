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

        curr = head
        count = 0
        while(curr):
            count += 1
            curr = curr.next
        mid = count//2
        curr = head
        for i in range(mid):
            curr = curr.next
        return curr
