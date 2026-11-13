class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1

        sort = [(nums[i], i) for i in range(len(nums))]

        sort = sorted(sort, key=lambda x: x[0])

        while i < j:
            val = sort[i][0] + sort[j][0]
            if val == target:
                return sorted([sort[i][1], sort[j][1]])
            elif val > target:
                j-=1
            else:
                i+=1

        return []
            
                
            
        