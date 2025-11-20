class Solution(object):
    combs = list()
    def combinationSum(self, candidates, target):
        self.combs = list()
        candidates.sort()
        self.recur(candidates, target, [])
        return self.combs
    def recur(self, candidates, target, arr):  
        if target == 0:
            self.combs.append(arr)
        if target > 0:
            for idx, val in enumerate(candidates):
                self.recur(candidates[idx:], target - val, arr + [val])
        
