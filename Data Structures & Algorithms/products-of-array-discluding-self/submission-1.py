
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [1] * length
        postfix = [1] * length

        # prefix products
        for i in range(1, length):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # postfix products
        for i in range(length - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        return [prefix[i] * postfix[i] for i in range(length)]