# 128. Longest Consecutive Sequence
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#Your algorithm should run in O(n) complexity.

import heapq
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        heapq.heapify(nums)
        longest, l = 1, 1
        last = heapq.heappop(nums)
        while nums:
            cur = heapq.heappop(nums)
            print last, cur
            if cur - last == 1:
                l += 1
            elif cur == last:
                continue
            else:
                if l > longest: longest = l
                l = 1
            last = cur
        return longest if longest > l else l

nums = [100, 4, 200, 1, 3, 2]
nums = [0,-1]
nums = [1,2,0,1]
print Solution().longestConsecutive(nums)

