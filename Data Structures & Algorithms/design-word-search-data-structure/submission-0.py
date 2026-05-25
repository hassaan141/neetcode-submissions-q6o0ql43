class TrieNode:
    def __init__(self):

        self.children = {}
        self.isTerminal = False

class WordDictionary:

    def __init__(self):

        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:

        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            
            node = node.children[char]
        
        node.isTerminal = True

    def search(self, word: str) -> bool:

        return self._search(word, self.root)
    
    def _search(self, word: str, node): 
        
        if len(word) == 0:
            return node.isTerminal

        for char in word:

            if char == '.':

                for c in node.children:
                    if self._search(word[1:], node.children[c]):
                        return True
                    
                return False
            else:
                if char not in node.children:
                    return False
                
                return self._search(word[1:], node.children[char])
