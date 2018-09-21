# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1 or not head:
            return head

        start = head
        bf_start = None
        end = start
        x = 1

        while end:
            if x == k:
                print x, bf_start.val if bf_start else bf_start, start.val, end.val, list2arr(head)

                (h, e) = self.reverse(bf_start, start, end)
                if not bf_start:
                    head = h
                print list2arr(head)
                bf_start = e
                start, end = e.next, e.next
                x = 1
            else:
                end = end.next
                x += 1
        return head

    def reverse(self, bf_start, start, end):
        next_start = end.next

        cur = start
        stack = []
        while cur != end:
            stack.append(cur)
            cur = cur.next

        while stack:
            cur.next = stack.pop()
            cur = cur.next

        start.next = next_start
        if bf_start:
            bf_start.next = end

        return end, start

def arr2list(lst):
    if not lst:
        return None

    head = ListNode(lst[0])
    cur = head

    for x in xrange(1, len(lst)):
        next = ListNode(lst[x])
        cur.next = next
        cur = next
    return head


def list2arr(head):
    ret = []
    next = head
    while next:
        ret.append(next.val)
        next = next.next
    return ret


a = [1,2]
#l = arr2list(a)
#print list2arr(l)

h = Solution().reverseKGroup(arr2list(a), 2)
print(list2arr(h))


