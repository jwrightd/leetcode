class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = []
        N = len(position)
        for idx in range(N):
            combined.append((position[idx], speed[idx]))
        combined.sort()
        print(combined)
        stk = []
        i = N - 1
        while i >= 0:
            pos, spd = combined[i]
            time = ((target - pos))/spd
            if not stk:
                stk.append((pos, spd))
            else:
                tPos, tSpd = stk[-1]
                t = ((target - tPos))/tSpd
                #print(time, t)
                if time > t:
                    stk.append((pos, spd))
            i -= 1

        # 2 4
        # 5 6
        # 8 8


        return len(stk)
        
