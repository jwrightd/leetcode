class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        # algo: freqmaps
        # counter for bull and cow
        # iterate through both strings
        # if chars match, bull
        # elif freqmap of guess char for secret > 0, increment cow
        # subtract from the freqmap for the secret
        cow = 0
        freq = defaultdict(int)
        bulls = set()
        for i in secret:
            freq[i] += 1
        N = len(secret)
        for idx in range(N):
            if secret[idx] == guess[idx]:
                freq[secret[idx]] -= 1
                bulls.add(idx)
        for idx in range(N):
            if idx not in bulls and guess[idx] in freq and freq[guess[idx]] > 0:
                cow += 1
                freq[guess[idx]] -=1
        return str(len(bulls)) + "A" + str(cow) + "B"
        
        
