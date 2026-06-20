class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        buckets = [[] for i in range(len(nums)+1)]

        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1

        for key, value in hashmap.items():
            buckets[value].append(key)
        
        res = []
        for i in range(len(buckets)-1, 0, -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res

        return res
