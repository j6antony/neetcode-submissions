class Solution:
    def maxArea(self, heights: List[int]) -> int:
        front = 0;
        end = len(heights) - 1;
        area = 0;
        while (front < end):
            if (heights[front] > heights[end]):
                greater = front
                lower = end;
            else:
                greater = end;
                lower = front;
            cur = heights[lower] * (end - front);
            if (cur > area):
                area = cur;
            if (lower > greater):
                end -= 1;
            else:
                front += 1;
        return area;