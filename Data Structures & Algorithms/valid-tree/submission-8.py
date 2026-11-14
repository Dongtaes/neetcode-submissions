class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False          # cycle
            visited.add(node)
            for child in adj[node]:
                if child == prev:
                    continue
                if not dfs(child, node):
                    return False      # stop early
            return True

        return dfs(0, -1) and len(visited) == n