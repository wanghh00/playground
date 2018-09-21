# Definition for singly-linked list.

import heapq

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = []
        head = ListNode(0) # dummy
        cur = head
        for one in lists:
            if not one:
                continue
            heapq.heappush(h, (one.val, one))

        while h:
            val, one = heapq.heappop(h)
            cur.next = one
            cur = cur.next
            if one.next:
                one = one.next
                heapq.heappush(h, (one.val, one))

        return head.next

