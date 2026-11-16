class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        normal = []
        for i in range(len(nums)):
            if i == 0:
                normal.append(1)
            else:
                normal.append(nums[i-1]*normal[i-1])


        rev = []
        for i in range(len(nums)):
            if i == 0:
                rev.append(1)
            else:
                rev.append(nums[-i]*rev[i-1])
                
        result = []
        i = 0
        while i < len(nums):
            result.append(normal[i]*rev[-i-1])
            i+=1

        return result