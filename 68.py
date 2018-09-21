# 68. Text Justification
class Solution(object):
    def __init__(self):
        self.idxLen = {}

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        lines, ret = [], []
        n = 0
        while n < len(words):
            one = self.oneLine(words, n, maxWidth)
            lines.append(one)
            n = one[-1] + 1
        
        for line in lines:
            numSlot = len(line) - 1 if len(line) > 1 else 1
            avgSpace = (maxWidth - sum(self.idxLen[x] for x in line)) / float(numSlot)
            numSpace = 0.0
            tmp = ""
            for x in xrange(len(line)-1):
                ns = int(avgSpace)
                if avgSpace + numSpace > int(avgSpace):
                    ns += 1
                tmp += words[line[x]] + ' '*ns
                numSpace = avgSpace - ns
            
            tmp += words[line[-1]]
            if len(line) == 1:
                tmp += ' '*int(avgSpace)

            print avgSpace, "'%s'" % tmp
            ret.append(tmp)
        
        return ret

    def oneLine(self, words, s_idx, maxWidth):
        """
        :rtype: idx used in this line
        """
        s = s_idx
        ret = [s]
        self.idxLen[s] = len(words[s])
        remain = maxWidth - self.idxLen[s]
        s += 1

        while s < len(words):
            self.idxLen[s] = len(words[s])
            if remain < self.idxLen[s] + 1:
                break
            ret.append(s)
            remain -= self.idxLen[s] + 1
            s += 1

        return ret

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

print Solution().fullJustify(words, maxWidth)
x = 11 / float(3)
y = 12 / 3


#print x, int(x), y, x > int(x)


        