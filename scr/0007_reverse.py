class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < -2 ** 31 or x > 2 ** 31 - 1:
            return 0
        nums = []
        sign = 1 if x >= 0 else -1
        x *= sign
        while x != 0:
            nums.append(x % 10)
            x = x // 10
        result = 0
        num_length = len(nums)
        for i, num in enumerate(nums):
            result += num * 10 ** (num_length - i - 1)
        result *= sign
        if result < -2 ** 31 or result > 2 ** 31 - 1:
            result = 0
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(123))
    print(solution.reverse(-123))
    print(solution.reverse(120))