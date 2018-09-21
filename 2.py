# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def show(self):
        x = self
        while x:
            print x
            x = x.next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret, cur = None, None
        upscale = 0
        while l1 and l2:
            tmp = ListNode()
            if cur:
                cur.next = tmp
                cur = tmp
            else:
                cur = tmp
                ret = cur

            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0

            cur.val = n1 + n2 + upscale
            if cur.val > 9:
                cur.val -= 10
                upscale = 1
            else:
                upscale = 0

            l1 = l1.next if l1
            l2 = l2.next if l2

        if upscale:
            cur.next = ListNode()
            cur.next.val = upscale

        return ret









        