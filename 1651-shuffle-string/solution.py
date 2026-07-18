class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        indChar = {}
        for idx, val in enumerate(indices):
            indChar[val] = s[idx]
        shuffled = []
        n = len(indices)
        for i in range(n):
            shuffled.append(indChar[i])
        return "".join(shuffled)
