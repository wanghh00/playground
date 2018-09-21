class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        # valid start point for idx in p
        sp = [[] for x in xrange(len(p)+1)]
        sp[0].append(0)

        si, pi = 0, 0
        while pi < len(p):

            has_star = pi < len(p) - 1 and p[pi+1] == "*"
            n_pi = pi + 2 if has_star else pi +1

            submatch = False
            for si in sp[pi]:
                if si == len(s):
                    submatch = True
                    sp[n_pi].append(si)
                    continue

                print "s=%s vs p=%s" % (s[si:], p[pi:])
                if has_star:
                    submatch = True

                    sp[n_pi].append(si)
                    for x in xrange(si, len(s)):
                        if s[x] == p[pi] or p[pi] == '.':
                            sp[n_pi].append(x+1)
                        else: break
                else:
                    if s[si] == p[pi] or p[pi] == '.':
                        sp[n_pi].append(si+1)
                        submatch = True

            print sp
            pi = n_pi
            if not submatch:
                return False

        return len(s) in sp[len(p)]

s = "abc"
p = "c*ab*c*"

xx = 'abc'
xx = 1 <0 and "12345"
#print Solution().isMatch(s, p)
#print Solution().isMatch("aa", "ab")
#print Solution().isMatch("ab", ".*")
#print Solution().isMatch("aab", "c*a*b")

s = "mississippi"
p = "mis*isp*."
#print Solution().isMatch(s, p)
#print Solution().isMatch("a", "ab*")
print Solution().isMatch("ab", ".*c")





