class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        dp = [0 for x in range(target+1)]
        dp[0] = 1

        for i in xrange(1, target+1):
            for x in nums:
                if i - x >= 0:
                    dp[i] += dp[i-x]
        return dp[target]


nums = [1,2,3]

Solution().combinationSum4(nums, 4)
