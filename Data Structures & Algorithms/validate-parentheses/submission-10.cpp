class Solution {
public:
    bool isValid(string s) {

        std::stack <char> p;

        if (s.size()%2 == 1) return false; 

        for(int i =0; i<s.size(); i++){

            if (s[i] == '[' || s[i] == '(' || s[i] == '{'){
                p.push(s[i]);
            }else if(s[i] == ']' || s[i] == ')' || s[i] == '}'){

                if (p.empty()) return false;

                if( (s[i] == ']' && p.top() != '[') ||  
                    (s[i] == ')' && p.top() != '(') ||
                    (s[i] == '}' && p.top() != '{')
                ){
                    return false;
                }else{
                    p.pop();
                }
            }
        }

        if(p.empty()){
            return true;
        }else{
            return false;
        }
    }
};
