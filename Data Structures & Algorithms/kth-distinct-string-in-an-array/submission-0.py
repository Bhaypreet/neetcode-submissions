class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dic = {}
        for i in range(len(arr)):
            if arr[i] in dic:
                dic[arr[i]] +=1
            else:
                dic[arr[i]] = 1
        a = k
        for item in arr:
            if dic[item] ==1 :
                a-=1
            if a == 0:
                return item

        return ""