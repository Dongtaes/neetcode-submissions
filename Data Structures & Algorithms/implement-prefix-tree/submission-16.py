class TreeNode:
    def __init__(self,children = None, val="", word = False):
        self.val = val
        self.word = word
        self.children = children if children is not None else {}
class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        p = self.root
        for i in range(len(word)):
            if word[i] in p.children:
                p = p.children[word[i]]
            else:
                p.children[word[i]] = TreeNode(val=word[i])
                p = p.children[word[i]]
        p.word = True

    def search(self, word: str) -> bool:
        p = self.root
        for i in range(len(word)):
            if word[i] in p.children:
                p = p.children[word[i]]
            else:
                return False
        return p.word
        

    def startsWith(self, prefix: str) -> bool:
        p = self.root
        for i in range(len(prefix)):
            if prefix[i] in p.children:
                p = p.children[prefix[i]]
                
            else:
                return False
        return True
        