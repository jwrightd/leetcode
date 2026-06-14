class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        output = ""
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for i in words:
            total = 0
            for j in range(len(i)):
                total += weights[alpha.index(i[j])]
            total = total % 26
            output += alpha[26 - total - 1]
        return output

        
