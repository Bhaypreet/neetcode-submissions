class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        dic = {}
        for i in range(len(order)):
            dic[order[i]] = i

        for i in range(len(words)-1):
            a = words[i]
            b = words[i+1]
            ans = 0
            for j in range(min(len(a),len(b))):
                if a[j] == b[j]:
                    ans+=1
                    continue
                else:
                    if dic[a[j]] > dic[b[j]]:
                        return False
                    else:
                        break
            if j+1 == ans:
                if len(a) > len(b):
                    return False

        return True