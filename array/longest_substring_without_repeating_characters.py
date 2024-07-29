class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        set_str = set()
        max_cnt = 0
        l = r = 0
        while(l <= r and r <= len(s)-1):
            if s[r] not in set_str:
                set_str.add(s[r])
                max_cnt = max(max_cnt, r-l + 1)
                r += 1
            else:
                set_str.remove(s[l])
                l += 1
            
        return max_cnt