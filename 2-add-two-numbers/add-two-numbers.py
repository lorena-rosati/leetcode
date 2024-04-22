# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def __init__(self):
        self.head = ListNode()
        self.curr = self.head

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        self.add(l1, l2, 0)
        return self.head.next
        

    def add(self, l1, l2, carry):
        if not l1 and not l2:
            if carry > 0:
                self.curr.next = ListNode(carry)
            return
        first = l1.val if l1 else 0
        second = l2.val if l2 else 0
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        sum = first + second + carry
        c = 0
        if sum > 9:
            c = 1
            sum = sum - 10
        self.curr.next = ListNode(sum)
        self.curr = self.curr.next
        self.add(l1, l2, c)
        
        