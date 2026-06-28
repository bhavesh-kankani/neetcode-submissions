class Solution:
    def anagram(self, s, t):
        d1, d2 = {}, {}
        for i in range(1, 27):
            d1[i], d2[i] = 0, 0
        for i in range(len(s)):
            d1[ord(s[i])-96] += 1
        for i in range(len(t)):
            d2[ord(t[i])-96] += 1
        return d1 == d2
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = set()
        final_ans = []
        for i in range(len(strs)):
            ans = []
            if strs[i] not in visited:
                for j in range(i+1, len(strs)):
                    if self.anagram(strs[i], strs[j]):
                        ans.append(strs[j])
                        visited.add(strs[j])
                visited.add(strs[i])
                ans.append(strs[i])
            if ans:
                final_ans.append(ans)
        return final_ans