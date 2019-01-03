class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        insertpos = 0
        for num in nums:
            if num != 0:
                nums[insertpos] = num
                insertpos +=1
        while(insertpos < len(nums)):
            nums[insertpos] = 0
            insertpos +=1
