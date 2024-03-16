# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head or head.next == None or k == 0:
            return head

        curr = head
        stack = []
        while curr:
            stack.append(curr)
            curr = curr.next
        l = len(stack)

        if k%l == 0:
            return head

        i = l - k%l
        j = l - 1
        if i>0:
            stack[i-1].next = None
        h = stack[i]
        stack[j].next = stack[0]

        return h
        