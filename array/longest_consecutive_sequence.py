class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lcs_set = set(nums)
        cnt = longest = 0
        for num in lcs_set:
            if (num -1) not in lcs_set:
                cnt =+ 1
                x = num
                while (x+1) in lcs_set:
                    cnt += 1
                    x += 1
                longest = max(cnt, longest)
        return longest