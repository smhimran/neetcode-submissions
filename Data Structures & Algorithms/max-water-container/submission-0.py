class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        maximumArea = 0

        while left < right:
            minHeight = min(heights[left], heights[right])
            current = minHeight * (right - left)
            maximumArea = max(maximumArea, current)

            if minHeight == heights[left]:
                left += 1
            else:
                right -= 1

        return maximumArea