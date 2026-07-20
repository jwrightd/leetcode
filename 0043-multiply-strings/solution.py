class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        # just simulate multiplication
        # 1 2 3
        # 4 5 6
        # algo, iterate through num2 nums, multiply with num1 items, if > 10 then shift
        output = [0] * (len(num1) + len(num2))
        listOne = list(num1)
        listTwo = list(num2)

        for idx, b in enumerate(listTwo[::-1]):
            for count, a in enumerate(listOne[::-1]):
                mult = int(a) * int(b)
                #print(mult, idx, count)
                #if mult >= 10:
                #    output[count + idx + 1] += 1
                #    output[count + idx] += mult % 10
                #else:
                output[count + idx] += mult
                #print(output)
        #print(output)
        i = 0
        while i + 1 < len(output):
            if output[i] >= 10:
                n = output[i] // 10
                output[i] -= 10 * n
                output[i + 1] += n
            i += 1
        res = [str(i) for i in output[::-1]]
        nonZero = 0
        for i in res:
            if i == "0":
                nonZero += 1
            else:
                break
        return "".join(res[nonZero:])


        
