class Solution(object):
    arr = []
    def letterCombinations(self, digits):
        self.arr = []
        self.recur(len(digits), digits, "")
        return self.arr
        """
        :type digits: str
        :rtype: List[str]
        """
    def recur(self,n, digits, st):
        if len(st) == n:
            self.arr.append(st)
        else:
            alpha = "abcdefghijklmnopqrstuvwxyz"
            current_digit = int(digits[0])
            possible_letters = alpha[(current_digit - 2) * 3 : (current_digit - 2) * 3 + 3] if current_digit < 7 else ["pqrs", "tuv", "wxyz"][current_digit - 7]
            #print(current_digit, possible_letters)
            for i in range(len(possible_letters)):
                self.recur(n, digits[1:], st + possible_letters[i])

        
