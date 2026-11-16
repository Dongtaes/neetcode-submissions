class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visit = set()
        permutations = []
        permutation = []

        def dfs(i):
            if i >= len(nums):
                permutations.append(permutation.copy())
                return
            for j in range(len(nums)):
                if j in visit:          # skip numbers already in this permutation
                    continue
                visit.add(j)
                permutation.append(nums[j])
                dfs(i + 1)
                permutation.pop()       # backtrack
                visit.remove(j)

        dfs(0)
        return permutations