# 466. Count The Repetitions

class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """

        for n in xrange(1, n1/n2+1):
            if self.obtain(s1*n, s2):
                return n1/n2/n


    def obtain(self, ss1, ss2):
        l1, l2 = len(ss1), len(ss2)
        if l1 < l2:
            return False

        x = y = 0
        while x < l1 and y < l2:
            if ss1[x] == ss2[y]:
                y += 1
            x += 1

        return y == l2

s1 = "acb"
s2 = "ab"
#print s1*2
#print Solution().obtain(s1, s2)
print Solution().getMaxRepetitions(s1, 4, s2, 2)