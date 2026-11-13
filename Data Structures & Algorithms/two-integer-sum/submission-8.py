class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        
        l = [(nums[i], i) for i in range(len(nums))]

        l = sorted(l, key=lambda x: x[0])

        while i < j:
            val = l[i][0] + l[j][0]
            if val == target:
                return sorted([l[i][1], l[j][1]])
            elif val > target:
                j-=1
            else:
                i+=1

        return []
            
                
            
        