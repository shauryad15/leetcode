from typing import List


def merge(self,intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    answer = []

    print(intervals)
    for i in range(0, len(intervals)):
        
        if not answer or (answer[-1][1] < intervals[i][0]):
            answer.append(intervals[i])
        
        else: 
            answer[-1][1] = max(answer[-1][1], intervals[i][1])
    return answer


print(merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))


    