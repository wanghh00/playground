# 139. Word Break
# Given a non-empty string s and a dictionary wordDict containing 
# a list of non-empty words, determine if s can be segmented into 
# a space-separated sequence of one or more dictionary words.

import heapq
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        hp = []
        dp = [0 for x in xrange(len(s)+1)]

        for one in wordDict:
            st_idx = 0
            while 1: 
                idx = s.find(one, st_idx)
                if idx == -1: break
                heapq.heappush(hp, [idx+1, idx+len(one)])
                st_idx = idx + 1

        dp[0] = 1
        print hp
        while hp:
            st, ed = heapq.heappop(hp)
            if dp[st-1] == 0: continue
            dp[ed] = 1

        print dp
        return dp[len(s)] == 1


s = "leetcode"
wordDict = ["leet", "code"]
s = "applepenapple"
wordDict = ["apple","pen"]

s = "aaaaaaa"
wordDict = ["aaaa","aaa"]

print Solution().wordBreak(s, wordDict)
