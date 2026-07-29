class Solution(object):
    def beautifulIndices(self, s, a, b, k):
        """
        :type s: str
        :type a: str
        :type b: str
        :type k: int
        :rtype: List[int]
        """
        # probably want to do in O(N)
        lenS = len(s)
        lenA = len(a)
        lenB = len(b)

        i_idx = []
        j_idx = []

        output = []
        n = lenS - lenA + 1
        m = lenS - lenB + 1

        for i in range(n):
            if s[i:i + lenA] == a:
                i_idx.append(i)
        for j in range(m):
            if s[j:j + lenB] == b:
                j_idx.append(j)
       # print(n)
        #exit()

        b_ptr = 0
        length = len(j_idx)
        for idx in i_idx:
            while b_ptr < length and j_idx[b_ptr] < idx - k:
                b_ptr += 1
            if b_ptr < length and j_idx[b_ptr] <= idx + k:
                output.append(idx)

                    
        return output

        
