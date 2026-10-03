class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        std::unordered_map<std::string, std::vector<std::string>> group;

        for (const std::string& str: strs){
            std::string ord_str = str;

            std::sort(ord_str.begin(), ord_str.end());

            group[ord_str].push_back(str);
        }

        std::vector<std::vector<std::string>> result;

        for (auto& pair : group){
            result.push_back(std::move(pair.second));
        }

        return result;
        
    }
};
