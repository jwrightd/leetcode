class Solution(object):
    def maximumCoins(self, coins, k):
        N = len(coins)    
        coins.sort()

        # has to start or end at a L/R boundary
        highest = 0
        current = 0
        # first we start at R and increase
        right = 0

        for left in range(N):
            while right < N and coins[right][1] <= coins[left][0] + k - 1:
                current += (coins[right][1] - coins[right][0] + 1) * coins[right][2]
                right += 1
            overlap = 0
            if right < N and coins[left][0] + k - 1 >= coins[right][0]:
                overlap = (coins[left][0] + k - 1) - coins[right][0] + 1
                overlap *= coins[right][2]
            highest = max(overlap + current, highest)
            current -= (coins[left][1] - coins[left][0] + 1) * coins[left][2]

        current = 0
        left = 0
        for right in range(N):
            current += (coins[right][1] - coins[right][0] + 1) * coins[right][2]

            while coins[left][1] + k - 1 < coins[right][1]:
                current -= (coins[left][1] - coins[left][0] + 1) * coins[left][2]
                left += 1
            
            # partial overlap
            overlap = 0
            if left < N and coins[left][0] + k - 1 < coins[right][1]:
                overlap = coins[right][1] - coins[left][0] - k + 1
                overlap *= coins[left][2]
            highest = max(highest, current - overlap)




                
        return highest
          
