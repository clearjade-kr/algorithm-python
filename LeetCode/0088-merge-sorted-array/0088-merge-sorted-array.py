class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Target: Merge sort two arrays nums1 and nums2 in-place

        i, j = 0, 0
        while j < n:
            if i >= m + j and nums1[i] == 0:
                nums1[i] = nums2[j]
                j += 1
            elif nums1[i] > nums2[j]:
                nums1[i:] = [nums2[j]] + nums1[i:m+n-1]
                j += 1
            i += 1