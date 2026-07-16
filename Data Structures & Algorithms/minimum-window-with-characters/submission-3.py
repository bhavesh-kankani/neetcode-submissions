class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_mp, s_mp = [0]*58, [0]*58
        required = formed = 0
        for i in range(len(t)):
            idx = ord(t[i]) - ord('A')
            if t_mp[idx] == 0:
                required += 1
            t_mp[idx] += 1
        
        l, r = 0, 0
        ans = (float("inf"), 0, 0)
        while r < len(s):
            r_idx = ord(s[r]) - ord('A')
            s_mp[r_idx] += 1

            if t_mp[r_idx] > 0 and t_mp[r_idx] == s_mp[r_idx]:
                formed += 1
            
            while l <= r and formed == required:
                if (r-l+1) < ans[0]:
                    ans = (r-l+1, l, r+1)
                l_idx = ord(s[l]) - ord('A')
                s_mp[l_idx] -= 1
                if t_mp[l_idx] > 0 and t_mp[l_idx] > s_mp[l_idx]:
                    formed -= 1
                l += 1
            r += 1

        return "" if ans[0] == float("inf") else s[ans[1]: ans[2]]
            
