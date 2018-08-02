class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l, r, minheight, water = 0, n-1, 0, 0 
        while l < r :
            while (l < r and height[l] <= minheight): 
                water += minheight - height[l]
                l += 1
            while (r > l and height[r] <= minheight):
                water += minheight - height[r]
                r -= 1
            minheight = min(height[l], height[r])
        return water