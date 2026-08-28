class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        

        result = 0
        
        while left < right:

            length = right - left
            height = min(heights[left], heights[right])
            area = length * height
            
            if area > result:
                result = area
                
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return result