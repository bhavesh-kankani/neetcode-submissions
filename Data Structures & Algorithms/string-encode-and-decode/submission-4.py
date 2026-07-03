class Solution:
    def encode(self, strs: List[str]) -> str:
        return ''.join([str(len(x)) + "#" + x for x in strs])

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        length = []
        i = 0
        decoded_string = []
        while i < len(s):
            if s[i] == "#":
                length = int(''.join(length))
                decoded_string.append(''.join([s[i+j+1] for j in range(length)]))
                i += (length+1)
                length = []
                continue
            length.append(s[i])
            i += 1
        return decoded_string
