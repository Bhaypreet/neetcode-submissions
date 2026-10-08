class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in range(len(s)):
            if not st:
                st.append(s[i])
            elif st:
                if s[i] == ")":
                    if st.pop() != "(":
                        return False
                    
                elif s[i] == "]":
                    if st.pop() != "[":
                        return False

                elif s[i] == "}":
                    if st.pop() != "{":
                        return False
                else:
                    st.append(s[i])
                
            
        if st:
            return False
        return True
                 