class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for direc in path.split('/'):
            if direc == '..':
                if stack:
                    stack.pop()
            elif direc not in ('', '.'):
                stack.append(direc)

        return '/' + '/'.join(stack)
