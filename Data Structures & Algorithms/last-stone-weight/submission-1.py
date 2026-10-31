import heapq as hp

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []

        for stone in stones:
            hp.heappush(pq, stone * -1)

        while len(pq) > 1:
            x = hp.heappop(pq) * -1
            y = hp.heappop(pq) * -1

            remaining = x - y

            if remaining > 0:
                hp.heappush(pq, remaining * -1)

        return pq[0] * -1 if len(pq) else 0