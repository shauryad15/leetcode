class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        org = nums.copy()
        nums.sort()
        i = 0
        j = len(nums) - 1
        out = []
        while(i < j):
            if(nums[i] + nums[j] == target):
                break
            elif (nums[i] + nums[j] > target):
                j -= 1
            else:
                i +=1
        for k in range(len(nums)):
            if(org[k] == nums[i] or org[k] == nums[j]):
                out.append(k)
        return out

        
        