class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # abs value = size
        # sign is direction + right, - left

        # two meet, bigger one stays. both same = both boom
        # all same speed
        
        # i think we need a stack
        stk = []
        idx = 0
        N = len(asteroids)
        while idx < N:
            curr = asteroids[idx]
            addAfter = True
            while stk and stk[-1] > 0 and curr < 0: # can explode here
                if stk[-1] == -curr:
                    stk.pop(-1)
                    addAfter = False
                    curr = 0
                elif stk[-1] < -curr:
                    stk.pop(-1)
                else:
                    addAfter = False
                    curr = 0
            if addAfter:
                stk.append(curr)
            idx += 1
        return stk




        return stk
        
