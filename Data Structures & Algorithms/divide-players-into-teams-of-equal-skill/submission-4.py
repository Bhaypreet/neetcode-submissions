class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        le = len(skill)//2
        ans = sum(skill)//le
        skill.sort()
        l = 0
        r = len(skill)-1
        b = 0
        

        while(l < r):
            if skill[l]+skill[r] == ans:
                b += skill[l]*skill[r]
                l+=1
                r-=1
            else:
                return -1

        return b


