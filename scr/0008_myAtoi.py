class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        nums = []
        sign = 1
        result = 0
        # str = str.lstrip()  #44ms to 24ms
        for i, ch in enumerate(str):
            if ch == ' ' and not nums:
                continue
            else:
                if ch.isdigit():
                    if not nums:
                        if i - 1 >= 0:
                            sign = -1 if str[i - 1] == "-" else 1
                    nums.append(int(ch))
                else:
                    if nums:
                        break
                    elif ch == '-' or ch == '+':
                        if i + 1 < len(str):
                            if not str[i+1].isdigit():
                                break
                    else:
                        return result
        num_length = len(nums)
        for i, num in enumerate(nums):
            result += num * 10 ** (num_length - i - 1)
        result *= sign
        if result < -2 ** 31:
            result = -2 ** 31
        if result > 2 ** 31 - 1:
            result = 2 ** 31 - 1
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.myAtoi("42"))
    print(solution.myAtoi("   -42"))
    print(solution.myAtoi("4193 with words"))
    print(solution.myAtoi("words and 987"))