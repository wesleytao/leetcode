# Method 1: Naive Approach: Hashmap

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list_single = {}
        for i in nums:
            if i in list_single:
                list_single[i] += 1
            else:
                list_single[i] = 1
        return next(key for key, value in list_single.items() if value == 1)
        
# Method 2: XOR Operators. (See https://hackernoon.com/xor-the-magical-bit-wise-operator-24d3012ed821)

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        v = 0
        for i in range(len(nums)):
            v ^= nums[i]
            
        return v