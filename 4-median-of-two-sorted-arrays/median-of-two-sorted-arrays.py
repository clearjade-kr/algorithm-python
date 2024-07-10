class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def find_kth(nums1, nums2, k):
            if not nums1:
                return nums2[k]
            if not nums2:
                return nums1[k]
            if k == 0:
                return min(nums1[0], nums2[0])
            len1, len2 = len(nums1), len(nums2)
            if len1 > len2:
                return find_kth(nums2, nums1, k)
            i = min(len1 - 1, k // 2)
            j = k - i - 1
            if nums1[i] > nums2[j]:
                return find_kth(nums1, nums2[j + 1:], k - j - 1)
            else:
                return find_kth(nums1[i + 1:], nums2, k - i - 1)

        len1, len2 = len(nums1), len(nums2)
        total_len = len1 + len2
        if total_len % 2 == 1:
            return find_kth(nums1, nums2, total_len // 2)
        else:
            return (find_kth(nums1, nums2, total_len // 2 - 1) + find_kth(nums1, nums2, total_len // 2)) / 2