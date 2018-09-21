class Solution(object):
    nums = set(['-','0','1','2','3','4','5','6','7','8','9'])
    def __init__(self):
        self.idx = 0
    
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        self.s = s                
        return self.parseList() if self.s[self.idx] == '[' else self.parseInt()
    
    def parseList(self):
        ret = []
        self.idx += 1
        while self.idx < len(self.s):
            cur = self.s[self.idx]
            if cur == ']':
                self.idx += 1
                return ret
            elif cur in Solution.nums:
                ret.append(self.parseInt())
            elif cur == ',':
                self.idx += 1
            elif cur == '[':
                ret.append(self.parseList())
        return ret
    
    def parseInt(self):
        ret = ""
        while self.idx < len(self.s):
            if self.s[self.idx] in Solution.nums:
                ret += self.s[self.idx]
                self.idx += 1
            else:
                break
        return int(ret)

test = "[123,[456,[789]]]"
print Solution().deserialize("123")
print Solution().deserialize("[123,456]")
print Solution().deserialize("[]")
print Solution().deserialize("[[]]")
print Solution().deserialize(test)

