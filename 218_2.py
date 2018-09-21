import heapq

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        heapx = []
        maxx = buildings[len(buildings)-1][0] + 1000

        for one in buildings:
            heapq.heappush(heapx, one)
            heapq.heappush(heapx, [one[1], maxx, 0])

        heapx.sort()
        print heapx

        heapq.heapify(heapx)

        heaph = []; heapq.heappush(heaph, [0, maxx])
        x, y = 0, 0
        ret = []
        while 
        #for i in xrange(len(heapx)):
            one = heapq.heappop(heapx)

            print one

            if one[2] or not heaph:
                heapq.heappush(heaph, [-one[2], one[1]])

            if one[2] > y:
                x, y = one[0], one[2]
                ret.append([x, y])
                print "newhigh: ", x, y
            elif one[2] == 0:
                while 1:
                    h = heapq.heappop(heaph)
                    if h[1] > one[0]:  # find second highest and longer 
                        break
                
                ret.append([one[0], -h[0]])
                x, y = one[0], -h[0]
                print "faildown: ", one[0], -h[0]

        return ret



buildings = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]

#output = [ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]

print Solution().getSkyline(buildings)