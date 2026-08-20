class Solution(object):
    def threeSumClosest(self, nums, target):
        closest_sum = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if curr_sum == target:
                    return curr_sum
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum
                if curr_sum < target:
                    l += 1
                else:
                    r -= 1
        return closest_sum                    

        