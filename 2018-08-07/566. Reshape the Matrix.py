#Naive solution:
class Solution:
    def matrixReshape(self, nums, r, c):       
        nums = [ nums[i][j] for i in range(len(nums)) for j in range(len(nums[0]))]
        if (r*c) != len(nums):
            return nums
        D = []
        i = 0
        for a in range(r):
            C = []
            for b in range(c):
                C.append(nums[i])
                i += 1
            D.append(C)
        return D

#More concise code:
def matrixReshape(self, nums, r, c):
    flat = sum(nums, [])
    if len(flat) != r * c:
        return nums
    tuples = zip(*([iter(flat)] * c))
    return map(list, tuples)