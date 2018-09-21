class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        grp = 2 * numRows - 2

        L = [''] * numRows

        for x in xrange(len(s)):
            grprem = x % grp
            y = grprem if grprem < numRows else 2 * numRows - grprem - 2
            L[y] += s[x]

        return ''.join(L)


test = "PAYPALISHIRING"

print 4 % 4
#test = "twckwuyvbihajbmhmodminftgpdcbquupwflqfiunpuwtigfwjtgzzcfofjpydjnzqysvgmiyifrrlwpwpyvqadefmvfshsrxsltbxbziiqbvosufqpwsucyjyfbhauesgzvfdwnloojejdkzugsrksakzbrzxwudxpjaoyocpxhycrxwzrpllpwlsnkqlevjwejkfxmuwvsyopxpjmbuexfwksoywkhsqqevqtpoohpd"

#Output: "PAHNAPLSIIGYIR"
print Solution().convert(test, 3)
