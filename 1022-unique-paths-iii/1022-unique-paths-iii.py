class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        i=j=0
        empty = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    empty += 1
                if grid[r][c] == 1:
                    i = r
                    j = c

        def dfs(r,c,remain):

            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == -1:
                return 0

            if grid[r][c] == 2:
                return 1 if remain == -1 else 0
            temp = grid[r][c]
            grid[r][c] = -1

            paths = (
                dfs(r+1,c,remain-1)+
                dfs(r-1,c,remain-1)+
                dfs(r,c+1,remain-1)+
                dfs(r,c-1,remain-1)
            )

            grid[r][c] = temp
            return paths

        return dfs(i,j,empty)

    