class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        i,j = 0,len(heights)-1
        water = 0
        while i<j:
            water = max(water, (j-i)*min(heights[i], heights[j]))
            if heights[i] < heights[j]:
                i+=1
            elif heights[j] < heights[i]:
                j-=1
            else:
                i+=1
                j-=1
        
        return water

