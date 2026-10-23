class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0



        for i in range(len(arr)-k+1):
            myans = sum(arr[i:i+k])
            if myans%k == 0:
                myans = myans//k
            else:
                myans /=k

            if myans >= threshold:
                ans+=1

        return ans