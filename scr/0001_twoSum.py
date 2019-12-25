import unittest


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        key_dict = dict()
        for i, num in enumerate(nums):
            if target - num in key_dict:
                return [i, key_dict[target - num]]
            else:
                key_dict[num] = i
        return []


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        del(self.solution)

    def test(self):
        res = self.solution.twoSum([2, 7, 11, 15], 9)
        x = sorted([0, 1]) == sorted(res)
        self.assertTrue(x)


if __name__ == '__main__':
    unittest.main()
