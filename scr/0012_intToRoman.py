class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Roman_dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
        #               9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        # keys = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        # if num < 1 or num > 3999:
        #     return ""
        # res = ""
        # i = 0
        # cur_sub = keys[i]
        # while num > 0:
        #     if num - cur_sub >= 0:
        #         res += Roman_dict[cur_sub]
        #         num -= cur_sub
        #     else:
        #         i += 1
        #         cur_sub = keys[i]
        # return res

        Roman_dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
                      9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        keys = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        if num < 1 or num > 3999:
            return ""
        res = ""
        for key in keys:
            n = num // key
            num -= key * n
            res += Roman_dict[key] * n
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.intToRoman(3 == "III"))
    print(solution.intToRoman(4) == "IV")
    print(solution.intToRoman(9) == "IX")
    print(solution.intToRoman(58) == "LVIII")
    print(solution.intToRoman(1994) == "MCMXCIV")
