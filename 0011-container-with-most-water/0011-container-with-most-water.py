class Solution(object):
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        max_a = 0
        while l < r:
            area = (r-l)*min(height[l],height[r])
            max_a = max(max_a, area)
            if height[l] < height[r]:
                l +=1
            else:
                r -= 1
        return max_a
       