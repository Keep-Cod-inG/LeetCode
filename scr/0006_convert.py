class Solution(object):
    # column wise 512 ms 13.7 MB
    # def convert(self, s, numRows):
    #     """
    #     :type s: str
    #     :type numRows: int
    #     :rtype: str
    #     """
    #     matrix = []
    #     result = ""
    #     ind = 0
    #     col = 0
    #     if numRows == 1:
    #         return s
    #     while ind < len(s):
    #         col_tmp = ["" for _ in range(numRows)]
    #         n = col % (numRows - 1)
    #         if n == 0:
    #             for i in range(numRows):
    #                 col_tmp[i] = s[ind]
    #                 ind += 1
    #                 if ind == len(s):
    #                     break
    #         else:
    #             col_tmp[numRows - n - 1] = s[ind]
    #             ind += 1
    #         col += 1
    #         matrix.append(col_tmp)
    #     numCols = len(matrix)
    #     for i in range(numRows):
    #         for j in range(numCols):
    #             result += matrix[j][i]
    #     return result

    # row wise 56 ms 11.9 MB
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rows = [[] for _ in range(numRows)]
        result = ""
        ind = 0
        col = 0
        if numRows == 1:
            return s
        while ind < len(s):
            n = col % (numRows - 1)
            if n == 0:
                for i in range(numRows):
                    rows[i].append(s[ind])
                    ind += 1
                    if ind == len(s):
                        break
            else:
                rows[numRows - n - 1].append(s[ind])
                ind += 1
            col += 1

        for row in rows:
            for c in row:
                result += c
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.convert("LEETCODEISHIRING", 3) == "LCIRETOESIIGEDHN")
    print(solution.convert("LEETCODEISHIRING", 4) == "LDREOEIIECIHNTSG")
