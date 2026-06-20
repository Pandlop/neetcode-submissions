class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for val in nums:
            seen[val] = seen.get(val,0) + 1
            if seen[val]>1:
                return True
        
        return False
        

        