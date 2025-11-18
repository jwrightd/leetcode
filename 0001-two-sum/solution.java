class Solution {
    public int[] twoSum(int[] nums, int target) {

        for (int i = 0; i < nums.length; i ++)
        {
            for (int x = i + 1; x < nums.length; x ++)
            {
                if (nums[i] + nums[x] == target)
                {
                    int[] twosum = {i, x};
                    return twosum;
                }
            }
        }
        return new int[2];
    }
}
