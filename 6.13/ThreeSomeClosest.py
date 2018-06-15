class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        sum_array = []
        n = len(nums)
        try:
            closest = nums[0] + nums[1] + nums[2]
        except Exception as e:
            print(e)
            exit()

        for first in range(n - 2):
            # initializing
            second = first + 1
            third = n - 1

            while second != third:
                thissum = nums[first] + nums[second] + nums[third]
                if thissum > target:
                    closest = closest if abs(target-closest) < abs(target-thissum) else thissum
                    third = third - 1
                elif thissum < target:
                    second = second + 1
                    closest = closest if abs(target - closest) < abs(target - thissum) else thissum
                else:
                    return thissum
        return closest


# solution = Solution()
# print(solution.threeSumClosest(nums=[1,2,5,10,11], target=12))

