class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # n rows of 10 seats
        # for each row, we can either do both 2-5 and 6-9, one of the groups, or none of the groups
        # algo
        # i am thinking some dictionary of nth row to a set of reserved seats for that row
        # then check each of the three intervals -- if 2-5 and 6-9 are both free, then we add 2
        # otherwise at max 1 interval may be added, and we add 1 if ANY of the three are valid
        # return result

        # ok so first ds
        rows = {}
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()
            rows[row].add(seat)
        def validLocation(seats, taken): # list of seats, set of taken
            for i in seats:
                if i in taken:
                    return False
            return True

        count = 0
        # now we iterate 1-n
        count += 2 * (n - len(rows))
        for i, reserved in rows.items(): #inclusive of N
            first =  validLocation([2, 3, 4, 5], reserved)
            second = validLocation([4, 5, 6, 7], reserved)
            third = validLocation([6, 7, 8, 9], reserved)
            if first and third:
                count += 2
            elif first or second or third:
                count += 1
        return count




        
