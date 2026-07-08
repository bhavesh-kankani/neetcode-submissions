class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i, j = 0, len(s)-1

        while i < len(s)//2:
            if not re.match(r'[a-zA-Z0-9]', s[i]):
                i += 1
                continue
            if not re.match(r'[a-zA-Z0-9]', s[j]):
                j -= 1
                continue
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
            
