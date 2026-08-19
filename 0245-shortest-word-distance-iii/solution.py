class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # we want some list of indices for our two desired words
        first = []
        second = []
        for idx, val in enumerate(wordsDict):
            if val == word1:
                first.append(idx)
            elif val == word2:
                second.append(idx)

        shortest = float('inf')
        # deal with same word1==word2 here:
        if word1 == word2:
            for idx in range(1, len(first)):
                shortest = min(shortest, first[idx] - first[idx - 1])
            return shortest
            # just want to check every 2 subsequent idx


        # now, algo
        # we want the shortest distance, we also know that these two lists are sorted
        # brute force is checking all pairs which is N2, but we can do in O(N) i think
        # we have a runnning min, we check current min between first and second at ptrs
        # if first[ptr] > second[ptr], we increment second_ptr
        # otherwise first ptr

        
        first_ptr = 0
        second_ptr = 0
        M, N = len(first), len(second)

        while first_ptr < M and second_ptr < N:
            current_dist = abs(first[first_ptr] - second[second_ptr])
            shortest = min(shortest, current_dist)
            if first[first_ptr] > second[second_ptr]:
                second_ptr += 1
            else:
                first_ptr += 1
        return shortest

        
