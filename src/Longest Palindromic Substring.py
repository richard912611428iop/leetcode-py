class Solution:
    # @return a string
    # @ref http://www.felix021.com/blog/read.php?2040 o(n) method
    def longestPalindrome(self, s):
        t = '#' + "#".join(s) + '#'
        m = len(t)
        mx = idx = 0
        p = [0 for i in range(m)]

        for i in range(1, m-1):
            p[i] = min(p[2*idx-i], mx-i) if mx > i else 1
            while i + p[i] < m and i - p[i] > -1 and t[i + p[i]] == t[i - p[i]]:
                p[i] += 1
            if i + p[i] > mx:
                idx = i
                mx = i + p[i]

        max_len = center_idx = 0

        for j in range(1, m-1):
            if p[j] > max_len:
                max_len = p[j]
                center_idx = j
        ret = t[center_idx-max_len+1:center_idx+max_len]
        return "".join(ret.split("#"))
