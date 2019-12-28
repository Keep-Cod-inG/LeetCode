class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s) > 0 and len(p) > 0:
            ch = s[-1]
            if p[-1] == ch or p[-1] == '.':
                return self.isMatch(s[:-1], p[:-1])
            elif p[-1] == '*':
                if len(p) >= 2:
                    if p[-2] == ch or p[-2] == '.':
                        return self.isMatch(s[:-1], p) or self.isMatch(s[:-1], p[:-2]) or self.isMatch(s, p[:-2])
                    else:
                        return self.isMatch(s, p[:-2])
                else:
                    return False
            else:
                return False
        if len(s) > 0 and len(p) == 0:
            return False
        if len(s) == 0 and len(p) == 0:
            return True
        if len(s) == 0 and len(p) > 0:
            if p[-1] == '*':
                if len(p) >= 2:
                    return self.isMatch(s, p[:-2])
                else:
                    return False
            else:
                return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.isMatch("aasdfasdfasdfasdfas", "aasdf.*asdf.*asdf.*asdf.*s") == True)
    print(solution.isMatch("aaa", "ab*a*c*a") == True)
    print(solution.isMatch("aaa", "aaaa") == False)
    print(solution.isMatch("aa", "a*") == True)
    print(solution.isMatch("ab", ".*") == True)
    print(solution.isMatch("aab", "c*a*b") == True)
    print(solution.isMatch("mississippi", "mis*is*p*.") == False)
