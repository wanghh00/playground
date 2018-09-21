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

        cur = head
        start = head
        bf_start = None
        bf_end = head

        x = 1
        while x < k - 1 and bf_end:
            bf_end = bf_end.next
            x += 1

        if not bf_end:
            return head
        
        #print x, bf_start, start.val, bf_end.val, list2arr(head)

        while bf_end.next:
            if x == k - 1:
                print x, bf_start.val if bf_start else bf_start, start.val, bf_end.val, list2arr(head)

                (h, e) = self.swap(bf_start, start, bf_end, k)
                if not bf_start:
                    head = h

                print list2arr(head)
                #bf_start = bf_end.next
                #start = bf_start.next.next
                #bf_end = start.next
                bf_start = e
                start = e.next
                bf_end = e.next
                if not bf_end: break

                print "hehe", bf_start.val, start.val, bf_end.val
                x = 1
                #print list2arr(head)
            else:
                bf_end = bf_end.next
                x += 1
        return head

    def swap(self, bf_start, start, bf_end, k):
        end = bf_end.next
        if not end:
            return

        if k == 2:
            start.next = end.next
            end.next = start
        else:
            af_end = end and end.next or None
            af_start = start.next

            end.next = af_start
            bf_end.next = start
            start.next = af_end
            end.next = af_start

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


