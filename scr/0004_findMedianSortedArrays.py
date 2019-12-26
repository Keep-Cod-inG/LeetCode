class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # i: start of L1, j: start of L2
        def findKth(L1, i, L2, j, k):
            if i >= len(L1):
                return L2[j + k - 1]
            if j >= len(L2):
                return L1[i + k - 1]
            if k == 1:
                return min(L1[i], L2[j])
            median1 = L1[i + k // 2 - 1] if i + k // 2 - 1 < len(L1) else None
            median2 = L2[j + k // 2 - 1] if j + k // 2 - 1 < len(L2) else None
            if median1 is None:
                return findKth(nums1, i, nums2, j + k // 2, k - k // 2)
            if median2 is None:
                return findKth(nums1, i + k // 2, nums2, j, k - k // 2)
            if median1 < median2:
                return findKth(nums1, i + k // 2, nums2, j, k - k // 2)
            else:
                return findKth(nums1, i, nums2, j + k // 2, k - k // 2)

        m = len(nums1)
        n = len(nums2)
        left = (m + n + 1) // 2
        right = (m + n + 2) // 2
        return (findKth(nums1, 0, nums2, 0, left) + findKth(nums1, 0, nums2, 0, right)) / 2


if __name__ == "__main__":
    solution = Solution()
    print(solution.findMedianSortedArrays([1, 2], [3, 4]))
