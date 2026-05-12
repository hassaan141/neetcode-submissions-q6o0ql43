class Solution:

    def encode(self, strs: List[str]) -> str:
        strr = ""

        for s in strs:
            strr += str(len(s)) + "%" + s
        
        return strr

    def decode(self, s: str) -> List[str]:
        
        i = 0
        out = []
        while i < len(s):

            num_start = i

            while s[i] != "%":
                i += 1
            
            number = s[num_start: i]
            print(number)

            # skip over the %

            i += 1

            # iterate over the letter
            word = s[i: i+int(number)]
            out.append(word)
            i += int(number)
        
        return out
            


