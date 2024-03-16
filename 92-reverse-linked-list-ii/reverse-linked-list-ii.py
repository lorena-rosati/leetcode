# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        count = 1
        h = head
        b = head
        first = True
        while count < left:
            first = False
            b = h
            h = h.next
            count += 1
        
        repeat = right - left + 1
        temp = h
        curr = temp
        prev = None
        a = None
        for i in range(repeat):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            a = curr
        
        if first:
            head = prev
        else:
            b.next = prev
        h.next = a

        return head