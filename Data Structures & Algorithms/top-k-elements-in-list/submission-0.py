class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i]+=1
                
        lis = []
        for i in range(k):
            max_key = max(dic, key=dic.get)
            lis.append(max_key)
            del dic[max_key]

        return lis