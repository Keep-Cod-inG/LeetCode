class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        position_dict = dict()
        start = 0
        end = 0
        length = 0
        for i, char in enumerate(s):
            if char not in position_dict or position_dict[char] <= start - 1:
                position_dict[char] = i

            else:
                cur_length = end - start
                if cur_length > length:
                    length = cur_length
                start = position_dict[char] + 1
                position_dict[char] = i
            end = i + 1
        cur_length = end - start
        if cur_length > length:
            length = cur_length
        return length


if __name__ == "__main__":
    solution = Solution()
    for s in ["abcabcbb", "bbbbb", "pwwkew"]:
        print(solution.lengthOfLongestSubstring(s))


