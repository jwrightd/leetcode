class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # all winners that are not in losers have not lost
        teams = set()
        losers = set()
        a0 = []
        a1 = []
        numLost = defaultdict(int)
        for winner, loser in matches:
            teams.add(winner)
            teams.add(loser)
            numLost[loser] += 1
        #print(numLost)
        for team in teams:
            if numLost[team] == 0:
                a0.append(team)
            elif numLost[team] == 1:
                a1.append(team)
        return[sorted(a0), sorted(a1)]

