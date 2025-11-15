class Solution(object):
    def change(self, amount, coins):
        return self.recur(amount, coins, len(coins) - 1, dict())
    
        # dp_arr[(ind, amount)]
    def recur(self, amount, coins, ind, dp_arr):
        if ind == 0:
            return 1 if amount % coins[0] == 0 else 0
        if (ind, amount) in dp_arr:
            notTake = dp_arr[(ind - 1, amount)]
        else:
            notTake = self.recur(amount, coins, ind - 1, dp_arr)
            dp_arr[(ind - 1, amount)] = notTake
        take = 0
        if coins[ind] <= amount:
            if (ind, amount - coins[ind]) in dp_arr:
                take = dp_arr[(ind, amount - coins[ind])]
            else:
                take = self.recur(amount - coins[ind], coins, ind, dp_arr)
                dp_arr[(ind, amount - coins[ind])] = take
        return take + notTake

    
        
