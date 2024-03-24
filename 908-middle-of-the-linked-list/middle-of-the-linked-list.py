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
        stack = []
        while(curr):
            stack.append(curr)
            curr = curr.next
        l = len(stack)
        mid = l//2
        return stack[mid]
