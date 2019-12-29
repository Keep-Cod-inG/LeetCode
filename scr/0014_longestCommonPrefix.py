class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortest_word = ""
        shortest = None
        for word in strs:
            if not shortest:
                shortest = len(word)
                shortest_word = word
            else:
                if len(word) < shortest:
                    shortest_word = word
                    shortest = len(word)
        res = shortest_word
        res_length = shortest
        while res_length > 0:
            temp = True
            for word in strs:
                temp &= (word[:res_length] == res)
                if not temp:
                    break
            if temp:
                return res
            else:
                res = res[:-1]
                res_length -= 1
        return ""


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl")
    print(solution.longestCommonPrefix(["dog", "racecar", "car"]) == "")
