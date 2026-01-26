class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        print(candidates)
        ret = []
        comb = []
        self.helper(candidates, target, 0, ret, comb)
        return ret

    def helper(self, candidates, target, idx, arr, curr):
        if target == 0:
            arr.append(curr)
            return
        if idx >= len(candidates):
            return
        #pick, ignore but with duplicates
        
        #pick
        nxtVal = target - candidates[idx]
        if nxtVal >= 0:
            self.helper(candidates, nxtVal, idx + 1, arr, curr + [candidates[idx]])
        
        #ignore
        i = idx + 1
        while i < len(candidates) and candidates[i] == candidates[idx]:
            i += 1
        self.helper(candidates, target, i, arr, curr)
            


