class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_mp = [0]*26
        s2_mp = [0]*26
        l = r = 0
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            s1_mp[ord(s1[i])-ord('a')] += 1
            s2_mp[ord(s2[i])-ord('a')] += 1
        if s2_mp == s1_mp:
            return True
        r = len(s1)
        while r < len(s2):
            s2_mp[ord(s2[l])-ord('a')] -= 1
            l += 1
            s2_mp[ord(s2[r])-ord('a')] += 1
            r += 1
            if s2_mp == s1_mp:
                return True
        return False
