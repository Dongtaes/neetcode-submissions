class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # borders flow always, and we need to check if the inward is higher than our outwards ->  then water can flow
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        pacific = set()
        atlantic = set()
        # m * n 
        # northbound pacific, southbound atlantic
        
        
        def dfs(visited,r,c,h):
            if not (0<=r<ROWS) or not(0<=c<COLS) or (r,c) in visited or not h <= heights[r][c]:
                return
            visited.add((r,c))
            for dX, dY in directions:
                dfs(visited,r+dX, c+dY, heights[r][c] )
             
        for col in range(COLS):
            dfs(pacific,0,col,heights[0][col])
            dfs(atlantic,ROWS-1,col,heights[ROWS-1][col])
        # westbound pacific, eastbound atlantic
        for row in range(ROWS):
            dfs(pacific, row, 0, heights[row][0])
            dfs(atlantic, row, COLS-1, heights[row][COLS-1])
        # union of the pacific and atlantic
        union = []

        for el in pacific:
            if el in atlantic:
                union.append(el)
        return union