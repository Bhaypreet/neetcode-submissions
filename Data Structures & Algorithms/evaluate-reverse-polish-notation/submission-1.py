class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for items in tokens:
            
            if items in ["+","-","*","/"]:
                b = st.pop()
                a = st.pop()
                
                if items == "+":
                    st.append(int(a+b))
                elif items == "-":
                    st.append(int(a-b))
                elif items == "/":
                    st.append(int(a/b))
                else:
                    st.append(int(a*b))
            else:
                st.append(int(items))

        return st[-1]