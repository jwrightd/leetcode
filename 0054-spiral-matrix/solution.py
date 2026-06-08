class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        total = m*n
        output = []

        direction = 0 # % 4 for dir

        rangeN = n
        rangeM = m

        current = 0
        # we repeat R, D, L, U on repeat
        while len(output) != total:
            if direction % 4 == 0: #R
                for i in range(rangeN):
                    output.append(matrix[current // n][current % n])
                    current += 1
                rangeM -=1
                current += n - 1
            elif direction % 4 == 1: #D
                for i in range(rangeM):
                    output.append(matrix[current // n][current % n])
                    current += n
                rangeN -=1
                current -= (n + 1)
            elif direction % 4 == 2: #L
                for i in range(rangeN):
                    output.append(matrix[current // n][current % n])
                    current -= 1
                rangeM -=1
                current += 1 - n
            else: #U
                for i in range(rangeM):
                    output.append(matrix[current // n][current % n])
                    current -= n
                current += n + 1
                rangeN -=1
            direction += 1
        return output

