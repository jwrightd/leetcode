class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 = c2 = None
        count1 = count2 = 0

        for n in nums:
            if n == c1:
                count1 += 1
            elif n == c2:
                count2 += 1
            elif count1 == 0:
                c1 = n
                count1 = 1
            elif count2 == 0:
                c2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        freq1 = freq2 = 0

        for n in nums:
            if n == c1:
                freq1 += 1
            elif n == c2:
                freq2 += 1

        output = []

        if freq1 * 3 > len(nums):
            output.append(c1)

        if freq2 * 3 > len(nums):
            output.append(c2)

        return output
