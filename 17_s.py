class Solution(object):
    def __init__(self):
        self.dct = {'0': '', '1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', 
            '7':'pqrs', '8':'tuv', '9':'wxyz'}
        self.ret = []

    # BFS solution
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return self.ret

        self.ret = [x for x in self.dct[digits[end]] ]

        for x in digits[1:]:
            tmp = []
            for one in self.ret:
                tmp.append(one+x)
            self.ret = tmp

        return self.ret 

a = '23'
#print [x for x in a]

print Solution().letterCombinations(a)

