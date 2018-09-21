import heapq

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        height = []

        for one in buildings:
            height.append([one[0], -one[2]])
            height.append([one[1], one[2]])

        height = sorted(height, cmp=self.cmpAB)
        print height

        pq = []
        ret = []
        heapq.heappush(pq, 0)
        prev = 0
        for one in height:
            print "handling", one

            if one[1] < 0:
                heapq.heappush(pq, one[1])
            else:
                for i in xrange(len(pq)):
                    if pq[i] == -one[1]: break
                print "remove ", pq[i]
                self.heapqremove(pq, i)

            print "pq ", pq

            cur = pq[0]
            if cur != prev:
                ret.append([one[0], -cur])
                print one[0], -cur
                prev = cur

        return ret

    @staticmethod
    def heapqremove(pq, idx):
        pq[idx] = pq[-1]
        pq.pop()
        heapq.heapify(pq)

    @staticmethod
    def cmpAB(a, b):
        return a[0] == b[0] and a[1] - b[1] or a[0] - b[0]


buildings = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]
b1 = [[1,2,1],[1,2,2],[1,2,3]]

#output = [ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]

print Solution().getSkyline(buildings)
print Solution().getSkyline(b1)