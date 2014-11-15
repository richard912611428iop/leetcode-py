class Solution:
    def foo(self, p, next_arr):
        p_len = len(p)
        next_arr[0] = -1
        k = -1
        j = 0
        while j < p_len - 1:
            if k == -1 or p[j] == p[k]:
                j += 1
                k += 1
                if p[j] != p[k]:
                    next_arr[j] = k
                else:
                    next_arr[j] = next_arr[k]
            else:
                k = next_arr[k]
        return

    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return haystack
        if len(haystack) == 0:
            return None
        n = len(haystack)
        m = len(needle)
        next_arr = [0 for i in range(m)]
        self.foo(needle, next_arr)
        i = j = 0
        while i < n and j < m:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next_arr[j]
        if j == m:
            return haystack[i - j:]
        else:
            return None
