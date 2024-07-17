class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
    
        i = 1  # Pointer for the place to insert
        for j in range(2, len(nums)):
            if nums[j] != nums[i] or nums[j] != nums[i - 1]:
                i += 1
                nums[i] = nums[j]
        return i + 1  # i is index, so length is i+1