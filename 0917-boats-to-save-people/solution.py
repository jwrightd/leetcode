class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # greedy
        # gonna want to match high/low
        people.sort()
        boats = 0
        N = len(people)
        # either we need to find the biggest diff
        # could do no dups
        left = 0
        right = N - 1
        while left < right:
            space = limit - people[right]
            if people[left] <= space:
                left += 1
            right -= 1
            boats += 1
        if left == right:
            boats += 1
        return boats

            
        
