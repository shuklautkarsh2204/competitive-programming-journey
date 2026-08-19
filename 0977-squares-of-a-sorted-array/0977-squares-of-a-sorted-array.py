class Solution(object):
    def sortedSquares(self, nums):
        sq_arr = []
        for i in nums:
            sq_arr.append(i*i)
        sq_arr.sort()
        return sq_arr  
        