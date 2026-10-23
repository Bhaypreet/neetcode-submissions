class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2,-1,-1):
            a = maxi
            maxi = max(maxi,arr[i])
            arr[i] = a
            
        return arr
