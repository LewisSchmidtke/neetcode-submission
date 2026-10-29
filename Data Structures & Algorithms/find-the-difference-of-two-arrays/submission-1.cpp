class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        set<int> set1(nums1.begin(), nums1.end());
        set<int> set2(nums2.begin(), nums2.end());

        vector<int> res1;
        vector<int> res2;

        for (int num1 : set1){
            if (set2.find(num1) == set2.end()){
                res1.push_back(num1);
            }
        }

        for (int num2 : set2){
            if (set1.find(num2) == set1.end()){
                res2.push_back(num2);
            }
        }


    return {res1, res2};
    }
};