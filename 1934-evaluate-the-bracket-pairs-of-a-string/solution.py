class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """

        kd = {}
        for k, v in knowledge:
            kd[k] = v
        idx = 0
        N = len(s)
        output = []
        start = s.find("(", idx)
        while start != -1:
            output.append(s[idx:start])
            end = s.find(")", start)
            key = s[start + 1:end]
            if key in kd:
                output.append(kd[key])
            else:
                output.append("?")
            idx = end + 1
            start = s.find("(", idx)

            
        output.append(s[idx:N])
        return "".join(output)

        
