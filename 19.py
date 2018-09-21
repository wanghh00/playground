# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = []
        cur = head
        while cur:
            temp.append(cur)
            cur = cur.next
        
        l = len(temp)
        if l == n:
            return temp[1]
        
        temp[l-n-1].next = temp[l-n+1]
        return head
        
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


