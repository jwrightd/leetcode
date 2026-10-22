class Solution(object):
    def strWithout3a3b(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: str
        """
        res = []
        while a != 0 or b != 0:
            if len(res) >= 2 and res[-1] == res[-2]:
                if res[-1] == "b":
                    res.append("a")
                    a -= 1
                else:
                    res.append("b")
                    b -= 1
            else:
                if a > b:
                    res.append("a")
                    a -= 1
                elif b > a:
                    res.append("b")
                    b -= 1
                else: # =
                    if len(res) > 0:
                        if res[-1] == "a":
                            res.append("b")
                            b -= 1
                        else:
                            res.append("a")
                            a -= 1
                    else:
                        res.append("a")
                        a -= 1
        return "".join(res)
