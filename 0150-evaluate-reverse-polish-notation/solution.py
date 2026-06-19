class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        #just use stack here i think?
        # push nums to stack
        # when we get operation, pop two nums, apply operation, push to stack
        # continue until nothing
        operations = "+-*/"
        stk = []
        while tokens:
            curr = tokens.pop(0)
            if curr in operations:
                second = stk.pop()
                first = stk.pop()
                if curr == "+":
                    stk.append(first + second)
                elif curr == "-":
                    stk.append(first - second)
                elif curr == "*":
                    stk.append(first * second)
                else:
                    val = first//second if first * second >= 0 else -((-first)//second)
                    stk.append(val)
            else:
                stk.append(int(curr))

        return stk[0]

