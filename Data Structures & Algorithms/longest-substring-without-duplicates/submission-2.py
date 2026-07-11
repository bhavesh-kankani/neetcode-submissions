class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        ans = r = l = 0
        while r < len(s):
            if s[r] in mp and mp[s[r]] >= l:
                l = mp[s[r]]+1
            ans = max(ans, r-l+1)
            mp[s[r]] = r
            r += 1
        return ans