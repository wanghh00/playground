import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        if k == 1: return matrix[0][0]

        stat = None
        x, y = 0, 0
        for n in xrange(0, k):
            if stat == None:
                if matrix[y+1][x] < matrix[y][x+1]:
                    stat = (y, x+1)
                else:
                    stat = (y+1, x)
            




        dim = len(matrix)
        h = []
        for y in xrange(dim):
            for x in xrange(dim):
                heapq.heappush(h, matrix[y][x])

        print heapq.nsmallest(k, h)[-1]

m = [[1,5,9,20],[2,6,10,21],[3,7,11,22],[4,8,12,23]]

Solution().kthSmallest(m, 16)
