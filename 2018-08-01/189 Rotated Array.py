class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for step in range(k):
            val = nums[-1]
            del nums[-1]
            nums.insert(0,val)