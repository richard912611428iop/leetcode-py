class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        dirs_stack = []
        middle = path.split('/')
        for i in middle:
            if i == "." or i == "":
                continue
            elif i == "..":
                if len(dirs_stack) != 0:
                    dirs_stack.pop()
            else:
                dirs_stack.append(i)
        result = "/"
        result += "/".join(dirs_stack)
        return result
