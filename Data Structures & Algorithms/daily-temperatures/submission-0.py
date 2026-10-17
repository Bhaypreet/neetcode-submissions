class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*(len(temperatures))

        st = []

        for i in range(0,len(temperatures)):

            while st and temperatures[i] > temperatures[st[-1]]:
                idx = st.pop()
                ans[idx] = i-idx

            st.append(i)

        return ans