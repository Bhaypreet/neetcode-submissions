class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        a = -1

        for i in range(r):
            if matrix[i][0] <= target <= matrix[i][c-1]:
                a = i
                break
        l = 0
        r = c-1

        while(l<=r):
            m = (l+r)//2

            if matrix[a][m] > target:
                r = m-1
                m = (l+r)//2
            elif matrix[a][m] < target:
                l = m+1
                m = (l+r)//2
            else:
                return True
        return False
