class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate_1 = candidate_2 = None
        count_1 = count_2 = 0

        for num in nums:
            if num == candidate_1:
                count_1 += 1
            elif num == candidate_2:
                count_2 += 1
            elif count_1 == 0:
                candidate_1 = num
                count_1 = 1
            elif count_2 == 0:
                candidate_2 = num
                count_2 = 1
            else:
                count_1 -= 1
                count_2 -= 1
        
        count_1 = count_2 = 0
        for num in nums:
            if num == candidate_1:
                count_1
            elif num == candidate_2:
                count_2
        return [n for n in (candidate_1, candidate_2) if nums.count(n) > len(nums) // 3]