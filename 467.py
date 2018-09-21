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
        s = set() # store found str as "a:2" mean start with 'a' lenght with 2, which is "ab"
        s.add("%s:1" % p[0])
        dp = [1 for x in xrange(l)] # dp[x] is length of seq at index x , for "abce" dp[2] = 3 as abc, dp[3] = 1 as e

        for x in xrange(1,l):
            s.add("%s:1" % p[x])
            diff = ord(p[x]) - ord(p[x-1])
            if diff == 1 or diff == -25:
                dp[x] = dp[x-1] + 1
                for n in xrange(x-dp[x]+1, x):
                    key = "%s:%s" % (p[n], x-n+1)
                    if key in s: break
                    s.add(key)
            else:
                dp[x] = 1

        print s
        return len(s)

p = "cac"
#p = "zab"
p = "abaab"
print Solution().findSubstringInWraproundString(p)
