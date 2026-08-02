class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # either num or diff
        # all odd or all even
        minOdd = float('inf')
        for i in nums1:
            if i % 2 == 1:
                minOdd = min(minOdd, i)
        
        def allOdd():
            nums2 = []
            for i in nums1:
                if i % 2 == 1:
                    nums2.append(i)
                else:
                    if i - minOdd >= 1 and (i - minOdd) % 2 == 1:
                        nums2.append(i - minOdd)
                    else:
                        return False
            return True
        
        def allEven():
            nums2 = []
            for i in nums1:
                if i % 2 == 0:
                    nums2.append(i)
                else:
                    if i - minOdd >= 1 and (i - minOdd) % 2 == 1:
                        nums2.append(i - minOdd)
                    else:
                        return False
            return True
        
        return allEven() or allOdd()
                    
            
