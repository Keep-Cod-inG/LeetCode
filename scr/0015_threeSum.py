class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if_used_dict = dict()
        twoSum_res = []
        for num in nums:
            if target - num in if_used_dict and not if_used_dict[target - num]:
                twoSum_res.append([target - num, num])
                if_used_dict[target - num] = True
                if_used_dict[num] = True
            if num not in if_used_dict:
                if_used_dict[num] = False
        return twoSum_res

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        pre_target = None
        for i, cur_target in enumerate(nums):
            if len(nums) - i >= 3:
                if cur_target != pre_target:
                    temp_res = self.twoSum(nums[i + 1:], -cur_target)
                    if temp_res:
                        for ele in temp_res:
                            tmp = ele.copy()
                            tmp = tmp + [cur_target]
                            res.append(tmp)
                    pre_target = cur_target
                else:
                    continue
            else:
                break
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
