class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for i in range(len(asteroids)):

            if asteroids[i] > 0:
                st.append(asteroids[i])

            elif len(st) == 0:
                st.append(asteroids[i])

            elif st[-1] < 0 and asteroids[i] < 0:
                st.append(asteroids[i])

            elif st[-1] > 0 and asteroids[i] < 0:
                if st[-1] == -1 * asteroids[i]:
                    st.pop()
                    continue

                while (len(st) > 0 and st[-1] > 0
                       and st[-1] < -1 * asteroids[i]):
                    st.pop()

                if len(st) == 0 or st[-1] < 0:
                    st.append(asteroids[i])

                elif st[-1] == -1 * asteroids[i]:
                    st.pop()

        return st