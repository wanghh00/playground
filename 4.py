import bisect

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        len1, len2 = len(nums1), len(nums2)
        mid = (len1 + len2) / 2
        
        mVal = (nums1[len1/2] + nums2[len2/2]) / 2

        n1 = bisect.bisect_left(nums1, mVal)
        n2 = bisect.bisect_left(nums2, mVal)
        print "mid=%s mVal=%s n1=%s n2=%s" % (mid, mVal, n1, n2)

        cur = n1 + n2

        if n1 == len1:
            x = nums1[len1-1]
            nums1[len1-1] = nums2[0]
            nums2[0] = x
            n1 = len1 - 1

        if n2 == len2:
            x = nums2[len2-1]
            nums2[len2-1] = nums1[0]
            nums1[0] = x
            n2 = len2 - 1


        vl1 = nums1
        vl2 = nums2
        while cur != mid:
            if cur > mid:  # move left
                cur -= 1
                if 


                if (vl1[n1] < vl2[n2] and n2) or n1 == 0:
                    n2 -= 1
                else:
                    n1 -= 1
            else: # move right
                cur += 1
                if (nums[n1] > nums[n2] and n2 != len2-1) or n1 == len1-1:
                    n2 += 1
                else:
                    n1 += 1

        print "n1=%s n2=%s" % (n1, n2) 
        print nums1[n1], nums2[n2]


    # binary locate i in list:nums[x:y] 
    # return x-1 if n < min(nums); len(nums) if x > max(nums)
    # return idx:i when x <= nums[i]
    def binLoc(self, nums, x, y, n):
        if x >= y:
            return x - 1 if n < nums[y] else y + 1

        m = (x + y) / 2

        if nums[m] == n: return m
        elif nums[m] < n:
            return self.binLoc(nums, m+1, y, n)
        return self.binLoc(nums, x, m-1, n)


l = [10, 20, 30]
ll = [1,2,3]
print Solution().findMedianSortedArrays(l, ll)
#print bisect.bisect_left(l, 3)