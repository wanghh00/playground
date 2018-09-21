class Solution(object):
    def __init__(self):
        self.w, self.h = 0, 0
        self.matrix = None
        self.table = None

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        self.matrix = matrix

        self.w, self.h = len(matrix[0]), len(matrix)

        # v-dir 1, h-dir 1, rect 1
        self.table = [[ [0,0,0] for x in xrange(self.w)] for y in xrange(self.h)]

        maxArea = 0
        for y in xrange(self.h-1, -1, -1):
            for x in xrange(self.w-1, -1, -1):
                if matrix[y][x] == '0': continue
                cur = self.table[y][x]
                cur[0] = 1 + self.getVnum(y+1,x)
                cur[1] = 1 + self.getHnum(y,x+1)
                if cur[0] * cur[1] > maxArea:
                    cur[2] = self.calArea(y,x)
                    maxArea = max(maxArea, cur[2])

        return maxArea

    def getVnum(self, y, x):
        if y >= self.h: return 0
        return self.table[y][x][0]

    def getHnum(self, y, x):
        if x >= self.w: return 0
        return self.table[y][x][1]

    def calArea(self, y, x):
        t = self.table[y][x]
        if t[0] == 1: # v-dir
            return t[0] * t[1]

        minW = t[1]
        maxArea = minW
        for i in xrange(1,t[0]):
            minW = min(minW, self.getHnum(y+i,x))
            maxArea = max(maxArea, (i+1)*minW)
        return maxArea

matrix = [
    ['1','0','1','0','0'],
    ['1','0','1','1','1'],
    ['1','1','1','1','1'],
    ['1','0','0','1','0']]

for x in matrix: print x
print Solution().maximalRectangle(matrix)