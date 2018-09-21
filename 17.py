class Solution(object):
    def __init__(self):
        self.dct = {'0': '', '1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', 
            '7':'pqrs', '8':'tuv', '9':'wxyz'}

    # BFS solution
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return self.ret

        ret = [x for x in self.dct[digits[0]] ]

        n = 1
        tmp = []
        while ret and n < len(digits):
            one = ret.pop()
            for x in self.dct[digits[n]]:
                tmp.append(one+x)
            if not ret:
                ret = tmp
                tmp = []
                n += 1
            
        return ret 

a = '23'
#print [x for x in a]

print Solution().letterCombinations(a)

