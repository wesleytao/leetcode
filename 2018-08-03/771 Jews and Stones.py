class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        collection = set(J)
        count =0
        for stone in S:
            if stone in collection:
                count =count+1
        return count