class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        i, j, sss = 0, 0, 0
        ll = len(nums)
        minlen = ll + 1

        while j < ll:
            sss += nums[j]
            j += 1

            while sss >= s:
                minlen = min(minlen, j - i)
                sss -= nums[i]
                i += 1

        return 0 if minlen == ll + 1 else minlen


s = 7
nums = [2,3,1,2,4,3]
s = 11
nums = [1,2,3,4,5]

print Solution().minSubArrayLen(s, nums)

