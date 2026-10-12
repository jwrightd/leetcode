class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output = [[1], [1, 1]]
        for num in range(3, numRows + 1):
            row = [1]
            for i in range(num - 2):
                row.append(output[-1][i] + output[-1][i + 1])
            row.append(1)
            output.append(row)



        return output[:numRows]
        
