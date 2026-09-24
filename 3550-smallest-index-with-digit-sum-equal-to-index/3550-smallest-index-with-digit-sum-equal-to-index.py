class Solution(object):
    def smallestIndex(self, nums):
        def digit_sum (n):
            sum = 0
            while n > 0:
                sum += n%10
                n //= 10
            return sum
        for i in range(len(nums)):
            if i == digit_sum(nums[i]):
                return i
        else:
            return -1    




        