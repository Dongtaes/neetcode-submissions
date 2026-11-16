class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(i,j,k,visit):
            if len(word) == k:
                return True 
            if (i,j) in visit or not 0<=i<ROWS or not 0<=j<COLS or board[i][j] != word[k]:
                return False
            res = False
            visit.add((i,j))
            for dx, dy in directions:
                nexti, nextj = dx+i, dy+j
                res |= dfs(nexti,nextj,k+1,visit)
            if res:
                return True
            visit.remove((i,j))
            return False

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                visit = set()
                if dfs(i,j,0,visit):
                    return True
        
        return False
