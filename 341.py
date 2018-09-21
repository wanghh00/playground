class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.curList = nestedList
        self.idx = 0
        self.stack = []
        

    def next(self):
        """
        :rtype: int
        """
        ret = self.curList[self.idx]
        self.idx += 1
        return ret        

    def hasNext(self):
        """
        :rtype: bool
        """

        #cur = self.curList[self.idx]
        while self.idx < len(self.curList) and type(self.curList[self.idx]) == list:
            self.stack.append([self.curList, self.idx+1])
            self.curList, self.idx = self.curList[self.idx], 0

        while self.stack and self.idx >= len(self.curList):
            self.curList, self.idx = self.stack.pop()

        return self.idx < len(self.curList)

a = [[1,1],2,[1,1]]
bb = [[1,1],2,[1,1]]
b = [[],[]]

tt = NestedIterator(bb)
out = []
while tt.hasNext():
    out.append(tt.next())
print out
