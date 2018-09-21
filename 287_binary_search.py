# 287. Find the Duplicate Number
# Given an array nums containing n + 1 integers where each integer is 
# between 1 and n (inclusive), prove that at least one duplicate number 
# must exist. Assume that there is only one duplicate number, find the duplicate one.
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

