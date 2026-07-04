class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        x, y, z = target
        # algo
        # for this to be true, we need to match each element to some triplet
        # additionally, we cannot include any triplets with elements greater than target

        # first, we filter

        first = set()
        second = set()
        third = set()
        for a, b, c in triplets:
            if a > x or b > y or c > z: # if any elements > than target
                continue 
            
            if not (a == x or b == y or c == z): # if no elements match
                continue
            
            first.add(a)
            second.add(b)
            third.add(c)
        
        # now we need to check our list and see if we can find a match at every index of target
        return x in first and y in second and z in third

