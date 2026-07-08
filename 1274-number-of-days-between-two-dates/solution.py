class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        # 2028 is leap year
        # if year divisible by 4, it is a leap year
        
        y1, m1, d1 = int(date1[:4]), int(date1[5:7]), int(date1[8:])
        y2, m2, d2 = int(date2[:4]), int(date2[5:7]), int(date2[8:])
        months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # let's just do date since 1971 jan 1
        def days_since(y, m, d):
            return 365 * (y - 1971) + sum(months_days[:m -1]) + d + sum([1 for i in range(1971, y) if i % 4 == 0]) + (y % 4 == 0 and (m > 2 or (m == 2 and d == 29))) - (y >= 2100)


        return abs(days_since(y1, m1, d1) - days_since(y2, m2, d2))


        
