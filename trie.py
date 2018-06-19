# class TrieNode:
class Trie:
    def __init__(self):
        self.end = False
        self.children = {}

    def all_words(self, prefix):
        if self.end:
            yield prefix

        for letter, child in self.children.items():
            yield from child.all_words(prefix + letter)

    '''
    Add the char to the trie as children
    '''
    def add(self, char):
        self.children[char] = Trie()

    def get_children(self):
        return self.children

    '''
    prefix : the input string 
    return : words matching the prefix 
    '''
    def search(self, prefix):
        cur = self
        for c in prefix:
            cur = cur.children.get(c)
            if cur is None:
                return  # No words with given prefix
        yield from cur.all_words(prefix)

    '''
    word : word to be inserted in trie
    '''
    def insert(self, word):
        node = self
        for c in word:
            if c not in node.get_children():
                node.add(c)
            node = node.children[c]
        node.end = True
