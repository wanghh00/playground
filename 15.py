class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        #print nums
        ret = []
        chkset = set()

        for x in xrange(len(nums)-2):
            if nums[x] in chkset:
                continue
            chkset.add(nums[x])
            
            rem = -nums[x]
            lo, hi = x + 1, len(nums) - 1
            chksubset = set()
            while lo < hi:
                result = nums[lo] + nums[hi] - rem
                if result > 0:
                    hi -= 1
                else:
                    if result == 0 and nums[lo] not in chksubset:
                        chksubset.add(nums[lo])
                        #print (x, lo, hi), (nums[x], nums[lo], nums[hi])
                        ret.append([nums[x], nums[lo], nums[hi]])
                    lo += 1
        return ret

nums = [-1, 0, 1, 2, -1, -4]
nums = [0,0,0,0]
print Solution().threeSum(nums)
