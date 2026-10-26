class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[0]*(2*numRows-1) for _ in range(numRows)]

        a =( 2*numRows-1)//2
        ans[0][a] = 1
        ans[numRows-1][0] = 1
        ans[numRows-1][-1] = 1

        for i in range(1,numRows):
            for j in range(1,2*numRows-2):
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j+1]

        lis = []
        for i in range(numRows):
            a = []
            for j in range(2*numRows-1):
                if ans[i][j] != 0:
                    a.append(ans[i][j])
            lis.append(a)

        return lis