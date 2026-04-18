class Node:
    def __init__(self):
        self.children=[None]*26
        self.is_word= False

class PrefixTree:

    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        curr = self.head
        for w in word:
            ind = ord(w) - ord('a') 
            if not curr.children[ind]:
                curr.children[ind]= Node()
            curr=curr.children[ind]
        curr.is_word=True
        


    def search(self, word: str) -> bool:
        curr= self.head
        for w in word:
            ind= ord(w)-ord('a')
            if not curr.children[ind]:
                return False
            curr=curr.children[ind]
        if curr.is_word:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        curr= self.head
        for w in prefix:
            ind= ord(w) - ord('a')
            if not curr.children[ind]:
                return False
            curr=curr.children[ind]
        return True
        
        