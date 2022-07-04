class Solution {
    public int[] twoSum(int[] nums, int target) {
         int[] Nums= new int[2];
        for (int i=0;i<nums.length;i++){
            for(int j=i+1;j<nums.length;j++){
                if(nums[i]+nums[j]==target){                   
                    Nums[0]=i;
                    Nums[1]=j;
                    return Nums;
                }
            }
        }
        return Nums;
    }
}