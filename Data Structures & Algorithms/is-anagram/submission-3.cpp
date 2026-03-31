class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()) return false;

        std::unordered_map<char, int> s_map;
        std::unordered_map<char, int> t_map;

        for(int i = 0; i<s.length(); i++){
            
            if (!s_map.count(s[i])){
                s_map[s[i]] = 1;
            }else{
                s_map[s[i]]++;
            }

            if (!t_map.count(t[i])){
                t_map[t[i]] = 1;
            }else{
                t_map[t[i]]++;
            }

        }

        for(auto c: s_map){
            char key = c.first;
            if(c.second != t_map[key]){
                return false;
            }
        }

        return true;

    }
};
