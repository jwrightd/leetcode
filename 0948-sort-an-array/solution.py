class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort
        # merge part
        

        def merge(left, right):
            output = []
            i, j = 0, 0
            n, m = len(left), len(right)

            while i < n and j < m:
                if left[i] < right[j]:
                    output.append(left[i])
                    i += 1
                else:
                    output.append(right[j])
                    j += 1
            while i < n:
                output.append(left[i])
                i += 1
            while j < m:
                output.append(right[j])
                j += 1
            return output


        def split(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr)//2

            left = split(arr[:mid])
            right = split(arr[mid:])

            return merge(left, right)
        
        return split(nums)
    
