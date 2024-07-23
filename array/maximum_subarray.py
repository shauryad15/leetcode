class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = -10**5 -1
        for i in range(len(nums)):
            current_sum += nums[i]
            if max_sum < current_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
            
        return max_sum
        