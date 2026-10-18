class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        # rolling hash
        N = len(s)
        ret = []
        seen = defaultdict(int)
        for i in range(N - 9):
            curr = s[i:i+10]
            seen[curr] += 1
            if seen[curr] == 2:
                ret.append(curr)
        return ret
