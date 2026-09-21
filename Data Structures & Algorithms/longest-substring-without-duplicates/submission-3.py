class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        ans = 0
        unique_chars = set()
        while r < len(s):
            
            if s[r] not in unique_chars:
                unique_chars.add(s[r])
                r += 1
            else:
                unique_chars.remove(s[l])
                l += 1
            ans = max(ans, r-l)
        return ans