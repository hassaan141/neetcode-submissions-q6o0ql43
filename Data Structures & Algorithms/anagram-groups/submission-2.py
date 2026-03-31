class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        """
        { k.   v. 
          {a:1, c:1, t:1}  : [act, cat, tac]
        }
        act cat
        a = 1 
        c = 1 
        t = 1

        """
        
        anagram_freq = {}
        for string in strs:
            
            word_freq = {}
            for w in string:
                
                if w not in word_freq:
                    word_freq[w] = 1
                else:
                    word_freq[w] += 1
            
            keys = tuple(sorted(word_freq.items()))

            if keys not in anagram_freq:
                anagram_freq[keys] = [ string ]
            else:
                anagram_freq[keys].append(string)

        out = []
        for i in anagram_freq.values():

            out.append(i)
        
        return out

        