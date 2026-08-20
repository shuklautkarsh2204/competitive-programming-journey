class Solution(object):
    def resultArray(self, nums):
        arr1 = []
        arr2 = []
        result = []
        arr1.append(nums[0])
        arr2.append(nums[1])
        for i in range(2,len(nums)):
            if arr1[-1] < arr2[-1]:
                arr2.append(nums[i])
            elif arr1[-1] > arr2[-1]:
                arr1.append(nums[i]) 

        result = arr1 + arr2
        return result          
        