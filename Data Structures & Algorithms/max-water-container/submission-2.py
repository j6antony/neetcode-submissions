class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1;
        maximum = min(heights[left], heights[right]) * (right - left);
        while (left < right):
            water = min(heights[left], heights[right]) * (right - left)
            maximum = max (water, maximum);
            if heights[left] < heights[right]:
                left+=1;
            else:
                right-=1;
        return maximum
        
