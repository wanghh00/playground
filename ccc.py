class Solution(object):
    def longestValidParentheses(self, s):
        pass


def subSetSum(lst, sum):
    dp = [0] * (sum + 1)
    dp[0] = 1
    print dp

    for n in lst:
        i = sum
        while i >= n:
            dp[i] += dp[i-n]
            print n, i, dp
            i -= 1

    return dp[sum]

#print Solution().longestValidParentheses(t2)
l = [1, 1, 2, 3, 4]
print subSetSum(l, 7)

