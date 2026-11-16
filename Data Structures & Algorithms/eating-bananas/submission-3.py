class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(k):
            hours = 0
            for bananas in piles:
                hours += (bananas + k - 1) // k
            return hours <= h

        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2
            if canEat(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res