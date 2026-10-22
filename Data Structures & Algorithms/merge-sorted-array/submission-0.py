class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while(n != 0):
            nums1.pop()
            n-=1
        while(len(nums2) != 0):
            a = nums2.pop()
            nums1.append(a)

        nums1.sort()
        