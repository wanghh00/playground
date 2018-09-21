
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        d = len(matrix[0])
        lo, hi = matrix[0][0], matrix[d-1][d-1]

        while lo < hi:
            mid = lo + (hi - lo) / 2
            count = 0; j = d - 1

            for i in xrange(d):
                while j>=0 and matrix[i][j] > mid: j -= 1
                count += (j + 1)

            print "lo=%s hi=%s mid=%s count=%s" % (lo, hi, mid, count)
            
            if count < k: lo = mid + 1
            else: hi = mid

        return lo



m = [[1,5,9,20],[2,6,10,21],[3,7,11,22],[4,8,12,23]]
m = [[11,21],[13,30]]
#tt = (0,1,"aaa")
#print Solution().kthSmallest(m, 1)
print Solution().kthSmallest(m, 2)
#print tt[2]