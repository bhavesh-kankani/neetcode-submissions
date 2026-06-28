class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        j = 0
        min_str_length = len(strs[0])
        for i in range(len(strs)):
            if len(strs[i]) < min_str_length:
                min_str_length = len(strs[i])
        while j < min_str_length:
            count = 0
            character = strs[0][j]
            for i in range(len(strs)):
                if strs[i][j] == character:
                    count += 1
                else:
                    return prefix
            if count == len(strs):
                prefix += strs[0][j]
            j += 1
        return prefix