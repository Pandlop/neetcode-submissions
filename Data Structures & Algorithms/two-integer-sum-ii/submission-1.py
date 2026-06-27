# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         hashmap = {}
        
#         for i in range(len(numbers)):
#             diff = target - numbers[i]
#             if diff in hashmap and hashmap[diff] != i+1:
#                 return [hashmap[diff],i+1]
#             hashmap[numbers[i]] = i+1
        
#         return []

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i,j = 0, len(numbers)-1
        
        while i<j:
            value = numbers[i] + numbers[j]
            if value == target:
                return [min(i,j)+1,max(i,j)+1]
            elif value < target:
                i+=1
            else:
                j-=1

        return []
                