class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        key = []
        i = 0
        while i < len(path):
            if path[i] == '/':
                if i > 0 and path[i-1] == '/':
                    i += 1
                    continue
                if key:
                    dir = ''.join(key)
                    if dir == '.':
                        pass
                    elif dir == '..':
                        if stack: stack.pop()
                    else:
                        stack.append(dir)
                    key = []
            else:
                key.append(path[i])
            i += 1
        if key:
            dir = ''.join(key)
            if dir == '.':
                pass
            elif dir == '..':
                if stack: stack.pop()
            else:
                stack.append(dir)
        print(stack)
        return '/' + '/'.join(stack)