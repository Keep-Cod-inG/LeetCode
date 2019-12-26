class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        result_length = 0
        for mid_left in range(len(s)):
            for k in [0, 1]:
                mid_right = mid_left + k
                cur_length = 0
                cur_result = ""
                left = mid_left
                right = mid_right
                while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                    cur_length = right - left + 1
                    cur_result = s[left:right + 1]
                    left -= 1
                    right += 1
                if cur_length >= result_length:
                    result = cur_result
                    result_length = cur_length
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome("babad"))