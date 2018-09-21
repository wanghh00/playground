# 128. Longest Consecutive Sequence
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#Your algorithm should run in O(n) complexity.

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best

nums = [100, 4, 200, 1, 3, 2]
nums = [0,-1]
nums = [1,2,0,1]
print Solution().longestConsecutive(nums)

