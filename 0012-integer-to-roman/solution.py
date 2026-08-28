class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        symbols = ["I", "IV", "V","IX", "X","XL", "L", "XC", "C","CD","D", "CM", "M"]
        vals = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        N = len(vals) - 1
        numeral = []
        while num > 0:
            while num >= vals[N]:
                numeral.append(symbols[N])
                num -= vals[N]
            N -= 1
        return "".join(numeral)

        

        
