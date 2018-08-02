class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                continue
            else:
                digits[i] = digits[i] + 1
                break

        if i == 0 and digits[0] == 0:
            digits.insert(0, 1)

        return digits