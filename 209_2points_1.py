class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        if total < s:
            return 0

        i, j = 0, 0
        sss = nums[0]

        while sss < s:
            j += 1
            sss += nums[j]

        print i, j
        minlen = j - i + 1
        ll = len(nums)
        for i in xrange(1, ll-1):
            sss -= nums[i-1]
            while sss < s and j < ll-1:
                j += 1
                sss += nums[j]
            print i, j
            if sss >= s:
                minlen = min(minlen, j-i+1)

        return minlen


s = 7
nums = [2,3,1,2,4,3]
s = 11
nums = [1,2,3,4,5]

print Solution().minSubArrayLen(s, nums)

