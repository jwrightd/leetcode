class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        
        # Array representing odd numbers only (size n // 2)
        # index i corresponds to the number (2*i + 1)
        is_prime = [True] * (n // 2)
        is_prime[0] = False  # 1 is not prime
        
        # Loop only through odd numbers starting from 3
        for i in range(1, int(n ** 0.5) // 2 + 1):
            if is_prime[i]:
                num = 2 * i + 1
                # Calculate the exact slice size mathematically to avoid len()
                # Step size in the index array is 'num'
                start_idx = (num * num) // 2
                slice_len = (n - 1 - num * num) // (2 * num) + 1
                
                is_prime[start_idx:n // 2:num] = [False] * slice_len
                    
        # Add 1 to the sum to account for the number 2 (the only even prime)
        return sum(is_prime) + 1
        
