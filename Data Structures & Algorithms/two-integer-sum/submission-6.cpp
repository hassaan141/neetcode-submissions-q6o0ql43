class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        // tuple of value and its index
        std::unordered_map<int, int> dict = {};

        for (int i = 0; i<nums.size(); i++){

            if (dict.size() == 0){
                dict[nums[i]] = i;
                continue;
            }

            int lookfor = target - nums[i];
    
            if (dict.contains(lookfor)){

                return {dict[lookfor], i};
            }
            else{

                dict[nums[i]] = i;
            }
        }

        return {};

    }
};
