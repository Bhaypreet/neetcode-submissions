class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        while(k != 0):
            a = nums.pop()
            nums.insert(0,a)
            k-=1
        