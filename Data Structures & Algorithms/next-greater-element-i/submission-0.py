class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {nums2[-1] : -1}
        for i in range(len(nums2)-1):
            r = i+1
            while(r < len(nums2)):
                if nums2[r] > nums2[i]:
                    dic[nums2[i]] = nums2[r]
                    break
                r+=1
            if r == len(nums2):
                dic[nums2[i]] = -1

        lis = []

        for i in range(len(nums1)):
            lis.append(dic[nums1[i]])
        
        return lis
