class Solution(object):
    def findDuplicate(self, nums):
        l, h = 1, len(nums)-1

        while l < h:
            mid = (l + h) / 2
            cnt = 0
            for x in nums:
                if x <= mid:
                    cnt += 1

            if cnt <= mid:
                l = mid + 1
            else:
                h = mid

        return l

nums = [1,3,4,2,2]
nums = [3,1,3,4,2]
nums = [2,2,2,2,2]
print Solution().findDuplicate(nums)

