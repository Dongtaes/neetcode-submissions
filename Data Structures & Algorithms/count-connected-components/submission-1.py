class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        adj = defaultdict(list)
        connected = []
        for s,d in edges:
            adj[s].append(d)
            adj[d].append(s)
        
        def dfs(i):
            visit.add(i)
            for child in adj[i]:
                if not child in visit:
                    dfs(child)
        res = 0
        for i in range(n):
            if not i in visit:
                dfs(i)
                res+=1
        return res