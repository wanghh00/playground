import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dct = {}
        for i in xrange(len(nums)):
            if nums[i] not in self.dct:
                self.dct[nums[i]] = []
            self.dct[nums[i]].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """

        if target not in self.dct:
            return -1

        l = self.dct[target]
        return l[random.randrange(len(l))]

a = [1,2,3,3,3]

for x in xrange(10):
    print Solution(a).pick(3)