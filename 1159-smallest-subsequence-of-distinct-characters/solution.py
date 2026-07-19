class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # monotonic stack
        # bcabc
        # b 
        # b c
        # a b c
        # cbacdcbc
        # c 
        # b
        # a
        # a c
        # a c d
        # a b c, so we pop if curr < top of stack and there arae still more occurrences in the str
        freq = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        visited = set()
        stk = []
        for i in s:
            #print(stk)
            if i in visited:
                freq[i] -= 1
                continue
            if not stk or i > stk[-1]:
                
                stk.append(i)

            else:
               # print(i, stk[-1])
                while stk and i < stk[-1] and freq[stk[-1]] > 0: 
                   # print(freq[stk[-1]], stk[-1])
                    visited.remove(stk[-1])
                    stk.pop(-1)
                stk.append(i)
            visited.add(i)
            freq[i] -= 1
        return "".join(stk)
            
            
