class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Roman_dict = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100,
                      'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5,
                      'IV': 4, 'I': 1}
        res = 0
        while len(s) > 0:
            if len(s) >= 2:
                if s[-2:] in Roman_dict:
                    res += Roman_dict[s[-2:]]
                    s = s[:-2]
                    continue
            if s[-1] in Roman_dict:
                res += Roman_dict[s[-1]]
                s = s[:-1]
            else:
                return 0
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt("III") == 3)
    print(solution.romanToInt("IV") == 4)
    print(solution.romanToInt("IX") == 9)
    print(solution.romanToInt("LVIII") == 58)
    print(solution.romanToInt("MCMXCIV") == 1994)
