class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return '-1'
        encoded_string = []
        for string in strs:
            for s in string:
                encoded_string.append(str(ord(s)) + '-')
            encoded_string.append('--')
        encoded_string.pop()
        encoded_string = ''.join(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if s == '-1':
            return []
        s = s.split('--')
        for i in range(len(s)):
            temp = []
            for x in s[i].split('-'):
                if x: temp.append(chr(int(x)))
            s[i] = ''.join(temp)
        return s
        
