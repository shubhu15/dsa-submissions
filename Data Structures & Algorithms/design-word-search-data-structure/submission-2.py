class Node:
    def __init__(self):
        self.children= {}
        self.end_word=False

class WordDictionary:

    def __init__(self):
        self.head = Node()
        
        

    def addWord(self, word: str) -> None:
        curr = self.head
        for w in word:
            if w!='.' and w not in curr.children:
                curr.children[w]=Node()
            curr=curr.children[w]
        curr.end_word= True
        
        

    def search(self, word: str) -> bool:

        def _search(j,node):
            curr= node

            for i in range(j,len(word)):
                if word[i]=='.':
                    for v in curr.children.values():
                        if _search(i+1, v):
                            return True
                    return False
                elif word[i] not in curr.children:
                    return False
                else:
                    curr=curr.children[word[i]]
            
            return curr.end_word

                

        return _search(0, self.head)
        
