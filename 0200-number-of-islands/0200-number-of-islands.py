from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        count = 0
        rows = len(grid)
        col = len(grid[0])

        for r in range(rows):
            for c in range(col):
                if grid[r][c] == "1":
                    count+=1
                    queue = deque()
                    queue.append((r,c))
                    grid[r][c] = "0"
                    while queue:
                        i,j = queue.popleft()
                        for dr,dc in directions :
                            nr= dr+i
                            nc= dc+j
                            if (0<=nr<rows and 0<=nc<col and grid[nr][nc]=="1"):
                                grid[nr][nc]="0"
                                queue.append((nr,nc))
        return count