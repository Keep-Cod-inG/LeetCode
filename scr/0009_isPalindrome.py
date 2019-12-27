class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            nums = []
            while x:
                nums.append(x % 10)
                x = x // 10
            num_length = len(nums)
            left = (num_length - 1) // 2
            right = num_length // 2
            while left >= 0 and right < num_length:
                if nums[left] != nums[right]:
                    return False
                left -= 1
                right += 1
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(121))
    print(solution.isPalindrome(-121))
    print(solution.isPalindrome(10))