class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        lis = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                else:
                    if words[j] in words[i]:
                        if words[j] not in lis:
                            lis.append(words[j])

        return lis