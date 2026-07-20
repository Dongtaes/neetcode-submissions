class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-el for el in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            n1 = heapq.heappop(stones)
            n2 = heapq.heappop(stones)
            dif = abs(n1 - n2)
            if dif == 0:
                continue
            heapq.heappush(stones, -dif)
        return -stones[0] if len(stones) ==   1 else 0