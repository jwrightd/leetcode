class Solution:
    def reorganizeString(self, s: str) -> str:
        # this is kind of like some counter
        # possible if most common char.count is not more than 1 more than the combined count of all others
        # need some kind of recursion
        # ex:
        # aaaabbbccc
        # 4 a, 3 b, 3 c
        # can do greedy to match a's

        # abababa[ccc]
        #however, let's say we always pick the next most popular char as the one to altenrate with

        # abacaba --1b, 2c
        # abacabacbc

        # so in general, our algorithm should be this: we always choose the highest freq letter that is not the prev char
        # so now what DS do we need

        # My first idea is this:
        # we use a maxheap, keyed on [freq, letter]
        # we have some string we store our output in
        
        import heapq

        output = []
        heap = []
        N = len(s)
        common = 0
        freq = defaultdict(int)
        for ch in s:
            freq[ch] += 1
            common = max(common, freq[ch])

        if common > 1 + N - common:
            return ""
        
        for ch in freq:
            heapq.heappush(heap, [-freq[ch], ch])
        
        while heap:
            negFreq, ch = heapq.heappop(heap)
            if not output or output[-1] != ch:
                output.append(ch)
                negFreq += 1
                if negFreq != 0:
                    heapq.heappush(heap, [negFreq, ch])
            else:
                nFreq2, ch2 = heapq.heappop(heap)
                output.append(ch2)
                if nFreq2 + 1 != 0:
                    heapq.heappush(heap, [nFreq2 + 1, ch2])
                heapq.heappush(heap, [negFreq, ch])
        

        return "".join(output)
