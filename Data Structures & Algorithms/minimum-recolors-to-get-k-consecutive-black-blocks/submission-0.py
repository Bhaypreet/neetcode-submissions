class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        lis = []
        for i in range(len(blocks)):
            if blocks[i] == "W":
                lis.append(1)
            else:
                lis.append(0)

        l = 0
        r = k-1
        mini = 100
        while(r < len(lis)):
            mini = min(mini,sum(lis[l:r+1]))
            l+=1
            r+=1

        return mini