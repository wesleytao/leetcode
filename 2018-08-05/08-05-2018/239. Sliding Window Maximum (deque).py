class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = collections.deque()
        res = []
        for i,n in enumerate(nums):
            while d and nums[d(-1)] < n:
                d.pop()
            d.append(i)
            if d[0] == i-k:
                d.leftpop()
            if i > n-k:
                res.append(nums[d[0]])
        return res