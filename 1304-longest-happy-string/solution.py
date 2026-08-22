class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # optimally we must alternate
        # or no
        # always choose most frequent unless last two are of same type
        strList = [] # want to join and return rather than recreating string (ON2 to ON)
        # lets just use heap for easy access
        import heapq
        heap = []
        for i in [[-a, "a"], [-b, "b"], [-c, "c"]]:
            heapq.heappush(heap, i)
        while heap:
            negVal, ch = heapq.heappop(heap)
            if negVal == 0:
                continue
            if len(strList) >= 2 and strList[-1] == ch and strList[-2] == ch: # cant have 3x
                if not heap:
                    return "".join(strList)
                else:
                    n2, ch2 = heapq.heappop(heap)
                    if n2 == 0:
                        continue
                    strList.append(ch2)
                    heapq.heappush(heap, [n2 + 1, ch2])
                    heapq.heappush(heap, [negVal, ch])
            else:
                strList.append(ch)
                heapq.heappush(heap, [negVal + 1, ch])
        return "".join(strList)




            
        
