class Solution:
    def longestPalindrome(self, s: str) -> str:
        ss = '#' + '#'.join(s) + '#'
        radius = [0]*len(ss)
        m = r = max_i = 0
        for i in range(len(ss)):
            radius[i] = min(radius[m]-i+m, radius[2*m-i])
            lf, ri = i-radius[i]-1, i+radius[i]+1
            while lf >= 0 and ri < len(ss) and ss[lf] == ss[ri]:
                lf -= 1
                ri += 1
                radius[i] += 1
            if ri > r:
                r = ri
                m = i
            if radius[i] > radius[max_i]:
                max_i = i
        return ''.join(ss[max_i-radius[max_i]:max_i+radius[max_i]+1].split('#'))


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome(input()))
