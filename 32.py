class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        score = [ 0 for x in xrange(len(s))]
        record = [-1]

        lengest, cur = 0, 0
        for x in xrange(len(s)):
            if s[x] == ')' and record:


                score[x] = 1
                score[record.pop()] = 1
            elif s[x] == '(':
                record.append(x)
        
        lengest, cur = 0, 0
        for x in xrange(len(s)):
            if score[x]:
                cur += 1
            else:
                lengest = lengest if lengest > cur else cur
                cur = 0
        lengest = lengest if lengest > cur else cur
        return lengest 

t1 = '))((())(())'
t2 = '((()())'

print Solution().longestValidParentheses(t2)