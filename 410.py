# 410. Split Array Largest Sum
# Given an array which consists of non-negative integers 
# and an integer m, you can split the array into m non-empty continuous 
# subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

import sys

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        length = len(nums)
        dp = [[0 for x in xrange(length)] for y in xrange(m+1)]

        dp[1][0] = nums[0]
        for x in xrange(1, length):
            dp[1][x] = dp[1][x-1] + nums[x]

        for y in xrange(2,m+1):
            for x in xrange(y-1, length):
                for j in xrange(y-1,x):
                    dp[y][x] = max(dp[y-1][i], )

        for one in dp:
            print one
    

nums = [7,2,5,10,8]

Solution().splitArray(nums, 2)
