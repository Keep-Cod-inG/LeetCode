class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        area_max = 0
        while left < right:
            area= min(height[left], height[right]) * (right - left)
            if area > area_max:
                area_max = area
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return area_max

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49)
