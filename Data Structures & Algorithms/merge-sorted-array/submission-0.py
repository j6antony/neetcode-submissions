class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        list1 = []
        for i in range(m):
            list1.append(nums1[i])
        total = len(nums1)
        counter = 0
        while total > counter:
            if len(list1) == 0:
                var = nums2.pop(0)
            elif len(nums2) == 0:
                var = list1.pop(0)
            elif list1[0] > nums2[0]:
                var = nums2.pop(0)
            else:
                var = list1.pop(0)
            nums1[counter] = var
            counter += 1
        