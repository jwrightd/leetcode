class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        c = n - 1
        digits[c] += 1
        if digits[c] != 10:
            return digits
        else:
            while digits[c] == 10 and c > 0:
                digits[c] = 0
                c -= 1
                digits[c] += 1
            if c == 0 and digits[c] == 10:
                digits[c] = 0
                return [1] + digits
            return digits


        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
