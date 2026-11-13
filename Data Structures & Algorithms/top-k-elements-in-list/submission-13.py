class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        h = []
        for num, count in counts.items():
            h.append((count,-num))
        
        heapq.heapify_max(h)
        
        res = []
        for _ in range(k):
            val = heapq.heappop_max(h)
            res.append(-val[1])

        return res
        
        