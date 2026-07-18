class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        # easy sliding window
        points = 0
        n = len(calories)
        
        # initial window
        T = sum(calories[:k])
        if T > upper:
            points += 1
        elif T < lower:
            points -= 1
        right = k
        while right < n:
            T = T + calories[right] - calories[right - k]
            if T > upper:
                points += 1
            elif T < lower:
                points -= 1
            right += 1
        return points
            
