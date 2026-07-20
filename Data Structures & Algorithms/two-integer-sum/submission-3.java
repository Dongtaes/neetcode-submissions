class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hm = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            int diff = target - nums[i];
            if(hm.containsKey(nums[i])){
                return new int[]{hm.get(nums[i]), i};
            }
            hm.put(diff, i);
        }
        return new int[]{0,0};
    }
}
