class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        pascal=[[1]]
        for n in range(1,numRows):
            temp_list = [1]
            for i in range(1,n):
                temp_list.append(pascal[n-1][i-1]+pascal[n-1][i])
            temp_list.append(1)
            pascal.append(temp_list)
                
        return pascal
        