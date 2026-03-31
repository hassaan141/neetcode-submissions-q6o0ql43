class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ''
        for i in strs:
            out = out + str(len(i)) + "$" + i
        
        print(out)
        return out


    def decode(self, s: str) -> List[str]:

        # 2$we3$say4$love3$yes
        i = 0
        out = []
        while i <len(s):
            c = i

            while s[c] != "$":
                c = c + 1

            print("i", i, "c", c)
            len_str = s[i: c]
            print(len_str)
            len_num = int(len_str)
            i = c + 1
            
            r_str = ""
            for j in range(i, i + len_num):
                r_str = r_str + s[j]
                i = i + 1
            
            print('I', i)
            out.append(r_str)
            print(out)
        
        return out
                



            

            




