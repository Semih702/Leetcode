class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ml=0
        mr=len(matrix)-1
        while ml<len(matrix) and matrix[ml][0]<=target:
            nr=len(matrix[0])-1
            nl=0
            while nl<=nr:
                nmid=(nl+nr)//2
                if matrix[ml][nmid]>target:
                    nr=nmid-1
                elif matrix[ml][nmid]<target:
                    nl=nmid+1
                else:
                    return True
            ml+=1
        return False