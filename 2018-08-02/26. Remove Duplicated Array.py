class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_p = 0
        second_p = 1
        while second_p < len(nums):
            if nums[second_p] == nums[first_p]:
                del nums[second_p]
            else:
                second_p = second_p+1
                first_p = first_p+1
        return len(nums)