class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        dic = []
        for i in range(len(boxes)):
            if boxes[i] == "1":
                dic.append(i)

        answer = []
        for i in range(len(boxes)):
            a = 0
            for j in range(len(dic)):
                a+=abs(dic[j]-i)

            answer.append(a)


        return answer