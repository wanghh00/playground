# 413. Arithmetic Slices

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A or len(A) < 3:
            return 0

        ll = len(A)
        #diff = [0 for x in xrange(ll)]
        dp = [0 for x in xrange(ll)]
        dp[1] = 1

        lastdiff = A[1] - A[0]
        for x in range(2, ll):
            diff = A[x] - A[x-1]
            if lastdiff == diff:
                dp[x] = dp[x-1] + 1
            else:
                lastdiff = diff
                dp[x] = 1

        print dp
        ret = 0
        for x in xrange(2, ll):
            if dp[x] > 1:
                ret += dp[x] -1
        return ret



A = [1,2,3,4]
A = [7,7,7,7]
print Solution().numberOfArithmeticSlices(A)

