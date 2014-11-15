class Solution:
    def __init__(self):
        self.buttons = {"1": "", "2": "abc", "3": "def",
                        "4": "ghi", "5": "jkl", "6": "mno",
                        "7": "pqrs", "8": "tuv", "9": "wxyz", "0": ""}

    def foo(self, digits):
        if len(digits) == 0:
            yield ""
            return
        if len(digits) == 1:
            for c in self.buttons[digits]:
                yield c
            return
        first = digits[0]
        rest = digits[1:]
        for ans in self.foo(rest):
            for c in self.buttons[first]:
                yield c + ans

    def letterCombinations(self, digits):
        return list(self.foo(digits))
