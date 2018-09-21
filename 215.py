import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        heapq.heapify(nums)

        for x in xrange(len(nums) - k + 1):
            ret = heapq.heappop(nums)

        return ret

nums = [3,2,3,1,2,4,5,5,6]

print Solution().findKthLargest(nums, 4) 
