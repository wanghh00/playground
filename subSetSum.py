
def subSetSum(nums, s):
    dp = [ 0 for x in xrange(s+1)]
    dp[0] = 1

    for n in nums:
        for i in xrange(s, n-1, -1):
            dp[i] += dp[i-n]
        print n, dp

    return dp[s]

nums = [1,2,3,4,5]
nums = [2,1,5,4,3]

print subSetSum(nums, 7)
