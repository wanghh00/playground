class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        ret = s[0]
        for x in xrange(len(s)-1):
            l, r = x, x
            while l >= 0 and r <= len(s)-1:
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            if r - l - 1 > len(ret):
                ret = s[l+1:r]

            if s[x] != s[x+1]: continue

            l, r = x, x + 1
            while l >= 0 and r <= len(s)-1:
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            if r - l - 1 > len(ret):
                ret = s[l+1:r]

        return ret

s = "123456789"
#print s[4:5]

in1 = "babad"
in2 = "cbbd"

print Solution().longestPalindrome(in1)
print Solution().longestPalindrome(in2)


