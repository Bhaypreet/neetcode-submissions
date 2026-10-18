class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        dic = {}
        for i in range(len(arr)):
            dic[i] = abs(x-arr[i])


        sorted_keys = [item[0] for item in sorted(dic.items(), key=lambda item: item[1])]
        lis = []

        # 2. Get the first k keys using slicing
        top_k_keys = sorted_keys[:k]
        for item in top_k_keys:
            lis.append(arr[item])
        lis.sort() 

        return lis