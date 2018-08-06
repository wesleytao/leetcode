class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = []
        index = [i for (i,(a,b)) in enumerate(zip(nums,sorted(nums))) if a!=b]
        return 0 if not index else index[-1]-index[0] + 1