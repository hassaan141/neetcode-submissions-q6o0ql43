class Solution {
public:
    int search(vector<int>& nums, int target) {
        
        int right = nums.size()-1, left = 0;

        if(nums[right]==target){
            return right;
        }

        if(nums[left] ==target){
            return left;
        }

        while(left<=right){

            int mid = (right+left)/2;
            
            if (target > nums[mid]){
                left = mid+1;
            }else if (target<nums[mid]){
                right = mid-1;
            }else{
                return mid;
            }
        }
        return -1;



        
    }
};
