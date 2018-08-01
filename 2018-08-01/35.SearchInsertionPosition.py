
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for idex,val in enumerate(nums):
            if nums[idex] < target:
                pass
            elif nums[idex]>=target:
                return idex
            else:
                raise ValueError("something wrong")
        return idex+1