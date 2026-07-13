class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = [0]*26
        l = r = max_len = max_freq = 0
        while r < len(s):
            length = r-l+1
            mp[ord(s[r]) - ord('A')] += 1
            max_freq = max(mp)
            if length - max_freq <= k:
                max_len = max(max_len, length)
            else:
                mp[ord(s[l]) - ord('A')] -= 1
                l += 1
            r += 1
        return max_len