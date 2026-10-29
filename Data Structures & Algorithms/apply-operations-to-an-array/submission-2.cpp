class Solution {
public:
    vector<int> applyOperations(vector<int>& nums) {
        int vector_size = nums.size();
        for (int i = 1; i < vector_size; i++){
            if (nums[i-1] == nums[i]){
                nums[i-1] *= 2;
                nums[i] = 0;
            }
        }

        int place_pointer = 0;
        for (int i = 0; i < vector_size; i++){
            if (nums[i] != 0){
                nums[place_pointer] = nums[i];

                if (place_pointer != i){
                    nums[i] = 0;
                }

                place_pointer += 1;
            }
        }

        return nums;
    }
};
