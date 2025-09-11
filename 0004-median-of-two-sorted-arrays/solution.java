class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int lenArr = nums1.length + nums2.length;
        int[] newArr = new int[lenArr];
        int m = 0;
        int n = 0;
        int count = 0;
        while (m < nums1.length || n < nums2.length)
        {
            if (m < nums1.length && n < nums2.length)
            {
                if (nums1[m] <= nums2[n])
                {
                    newArr[count] = nums1[m];
                    m ++;
                }
                else
                {
                    newArr[count] = nums2[n];
                    n++;
                }
            }
            else if (m < nums1.length)
            {
                newArr[count] = nums1[m];
                m++;
            }
            else
            {
                newArr[count] = nums2[n];
                n++;
            }   
            count ++;
        }
        for (int i : newArr)
        {
            System.out.print(i + " ");
        }
        System.out.println();
        double med = (newArr.length % 2 == 1) ? (double)(newArr[newArr.   length/2]) : ((double)(newArr[newArr.length/2 - 1]) + (double)(newArr[newArr.length/2]))/2.0;
        return med;
    }
        
}
