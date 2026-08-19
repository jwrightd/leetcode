class Solution(object):
    def beautifulIndices(self, s, a, b, k):
        """
        :type s: str
        :type a: str
        :type b: str
        :type k: int
        :rtype: List[int]
        """
        lenS = len(s)
        lenA = len(a)
        lenB = len(b)
        # i is beautiful if it starts an instance of a in s
        # there is an instnce of b in s that starts within k units of i
        # algo: get i, j candidates
        # two pointers, one for each array of candidates
        # iterate through i candidates, increment j candidates if gap is too large

        i_candidates = []
        j_candidates = []

        for i in range(lenS - lenA + 1):
            if s[i:i + lenA] == a:
                i_candidates.append(i)
        
        for i in range(lenS - lenB + 1):
            if s[i:i + lenB] == b:
                j_candidates.append(i)
        
        i_ptr = 0
        j_ptr = 0
        N, M = len(i_candidates), len(j_candidates)

        beautiful_indices = []

        while i_ptr < N and j_ptr < M:
            curr_candidate = i_candidates[i_ptr]
            if abs(j_candidates[j_ptr] - curr_candidate) <= k:
                beautiful_indices.append(curr_candidate)
                i_ptr += 1
            else:
                if curr_candidate - j_candidates[j_ptr] > k:
                    j_ptr += 1
                else:
                    i_ptr += 1

        





        return beautiful_indices
        
