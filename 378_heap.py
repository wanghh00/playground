import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        h = []

        for x in xrange(n):
            heapq.heappush(h, (matrix[0][x], 0, x))

        for i in xrange(1, k):
            t = heapq.heappop(h)
            if t[1] == n - 1:
                continue
            heapq.heappush(h, (matrix[t[1]+1][t[2]], t[1]+1, t[2]))

        return heapq.heappop(h)[0]



m = [[1,5,9,20],[2,6,10,21],[3,7,11,22],[4,8,12,23]]

#tt = (0,1,"aaa")
print Solution().kthSmallest(m, 3)
print Solution().kthSmallest(m, 12)
#print tt[2]