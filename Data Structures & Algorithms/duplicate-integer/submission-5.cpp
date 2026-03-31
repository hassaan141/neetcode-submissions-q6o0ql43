class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {

        std::unordered_set<int> list;

        for(int i =0; i<nums.size(); i++){
            
            if(list.count(nums[i])){
                return true;
            }else{
                list.insert(nums[i]);
            }
        }

        return false;
    }

};