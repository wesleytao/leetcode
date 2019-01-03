class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        premax = nums[0]
        premin = nums[0]
        max_ = premax
        for num in nums[1:]:
            if num < 0:
                premin,premax = premax,premin
            premin = min(num,premin*num)
            premax = max(num,premax*num)
            # print("current premin {} premax {}".format(premin,premax))
            max_ = max(max_,premax)
        return max_
