class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxia = 0
        maxh = 0
        l = 0
        r = len(heights)-1
        while(l < r):
            
            if heights[l] > heights[r]:
                area = (r-l)*heights[r]
                r-=1
            else:
                area = (r-l)*heights[l]
                l+=1
            
            maxia = max(maxia,area) 

        return maxia
