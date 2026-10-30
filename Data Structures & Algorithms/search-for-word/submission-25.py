class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        visited = set()
        direction = [(1,0), (-1,0) , (0,1), (0,-1)]
        def dfs(row, col, i):
            if len(word) == i:
                return True
            if (row,col) in visited or not(0<=row<ROW) or not(0<=col<COL) or board[row][col] != word[i]:
                return False
            visited.add((row,col))
            for dire in direction:
                if dfs(row+dire[0], col+dire[1],i+1):
                    return True
            visited.remove((row,col))
            return False
            
        for row in range(ROW):
            for col in range(COL):
                if dfs(row,col,0):
                    return True
        
        return False