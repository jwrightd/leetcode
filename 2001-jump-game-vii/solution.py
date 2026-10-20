class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        if s[-1] == "1":
            return False

        N = len(s)
        queue = [0]
        farthest = 0
        while queue:
            idx = queue.pop(0)
            if idx == N - 1:
                return True
            
            start = max(farthest + 1, idx + minJump)
            end = min(N - 1, idx + maxJump)
            for i in range(start, end + 1):
                if s[i] == "0":
                    queue.append(i)
            farthest = max(farthest, end)


        return False
