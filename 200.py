# 200. Number of Islands
# Given a 2d grid map of '1's (land) and '0's (water), count the number 
# of islands. An island is surrounded by water and is formed by connecting 
# adjacent lands horizontally or vertically. You may assume all four edges of 
#the grid are all surrounded by water.

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        num = 0
        for y in xrange(len(grid)):
            for x in xrange(len(grid[0])):
                if grid[y][x] != '1': continue
                
                name = chr(ord('a')+num)
                grid[y][x] = name
                num += 1
                q = []
                q.append((y,x))
                i = 0

                while i < len(q):
                    ny,nx = q[i]
                    print ny, nx
                    if ny < len(grid)-1 and grid[ny+1][nx] == '1':
                        grid[ny+1][nx] = name
                        q.append((ny+1, nx))
                    if nx < len(grid[0]) - 1 and grid[ny][nx+1] == '1':
                        grid[ny][nx+1] = name
                        q.append((ny,nx+1))
                    if nx > 0 and grid[ny][nx-1] == '1':
                        grid[ny][nx-1] = name
                        q.append((ny,nx-1))
                    if ny > 0 and grid[ny-1][nx] == '1':
                        grid[ny-1][nx] = name
                        q.append((ny-1,nx))
                    i += 1

                for one in grid:
                    print one
                print '--------------'

        return num

grid = [['1','1','0','0','0'],['1','1','0','0','0'],
    ['0','0','1','0','0'],['0','0','0','1','1']]
grid = [["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]
#print chr(ord('a') + 1)
for one in grid:
    print one

print Solution().numIslands(grid)


