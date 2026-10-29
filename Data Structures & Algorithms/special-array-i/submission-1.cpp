class Solution {
public:
    bool isArraySpecial(vector<int>& nums) {
        bool even {false};

        if (nums[0] % 2 == 0) {
            even = true;
        }

        int size;
        bool is_even;
        size = nums.size();

        for (int i = 1; i<size; ++i){
            is_even = nums[i] % 2 == 0;

            if (is_even == even){
                return false;
            }

            even = is_even;
        }

        return true;

    }
};