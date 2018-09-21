# 467. Unique Substrings in Wraparound String

class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        if not p:
            return 0

        l = len(p)
        s = set()
        dp = [[ 0 for x in xrange(l)] for y in xrange(l)] # if p[x:y+1] if good then 1

        for x in xrange(l):
            dp[x][x] = 1
            s.add(p[x])

        for x in xrange(l):
            for y in range(x+1,l):
                if not dp[x][y-1]: continue
                diff = ord(p[y]) - ord(p[y-1])
                if diff == 1 or diff == -25:
                    dp[x][y] = 1
                    s.add(p[x:y+1])
                print "dp[%s][%s]=%s" % (x, y, dp[x][y])
        print s
        return len(s)

p = "cac"
p = "zab"
print Solution().findSubstringInWraproundString(p)
