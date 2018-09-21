# 72. Edit Distance
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        # state dp[i][j] to be the minimum number of operations to convert word1[0..i - 1] to word2[0..j - 1]
        m, n = len(word1), len(word2)
        dp = [ [0 for x in xrange(n+1)] for y in xrange(m+1)]
        
        for i in xrange(1, m+1):
            dp[i][0] = i
        for j in xrange(1, n+1):
            dp[0][j] = j

        for i in xrange(m):
            for j in xrange(n):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j]+1, min(dp[i+1][j]+1, dp[i][j+1]+1))
        self.dispDP(dp)

        return dp[m][n]



    def dispDP(self, dp):
        for y in xrange(len(dp)):
            one = ""
            for x in xrange(len(dp[0])):
                s1 = word1[:y] if y > 0 else ''
                s2 = word2[:x] if x > 0 else ''
                one += '%s:%s|%s:%s=%s\t' % (y, s1, x, s2, dp[y][x])
            print one



word1 = "horse"
word2 = "ros"

print Solution().minDistance(word1, word2)
