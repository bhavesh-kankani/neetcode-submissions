class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        prefix = ""
        for i in range(len(strs[0])):
            a = strs[0][i]
            flag = True
            for j in range(len(strs)):
                if strs[j][i] != a:
                    flag=False
                    return prefix
            if flag:
                prefix += a
        return prefix
