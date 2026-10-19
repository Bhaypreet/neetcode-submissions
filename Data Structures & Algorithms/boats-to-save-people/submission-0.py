class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        summ = 0
        l = 0
        r = len(people)-1

        while(l<=r):

            if l == r:
                if people[l] <= limit :
                    summ+=1
                    r-=1
                    l+=1

            elif people[l]+people[r] <= limit :
                summ+=1
                l+=1
                r-=1
            else:
                if people[r] <= limit:
                    summ+=1
                    r-=1

        return summ