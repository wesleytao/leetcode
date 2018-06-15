class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i !=j:
        #             if nums[i]+nums[j]==target:
        #                 return [i,j]
        # return None
        res = dict()
        for i in range(len(nums)):
            this_key = target - nums[i]
            try:
                j = res[nums[i]]
                return ([j, i])
            except Exception as e:
                res[this_key] = i
                pass
