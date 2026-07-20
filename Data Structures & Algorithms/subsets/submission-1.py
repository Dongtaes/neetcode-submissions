class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtracking(i, path):
            if i>= len(nums):
                res.append(path.copy())
                return
            # with the index
            path.append(nums[i])
            backtracking(i+1, path)
            path.pop()

            # without the index
            backtracking(i+1, path )
        backtracking(0,[])
        return res