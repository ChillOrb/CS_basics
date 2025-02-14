"""

208. Implement Trie (Prefix Tree)
Medium

5115

77

Add to List

Share
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 

Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.

"""

# V0
# IDEA : USE dict AS data structure (# TrieNode: is dict, or hashmap)
class Trie(object):            
    def __init__(self):
        self.root = {} # TrieNode: is dict, or hashmap       
 
    def insert(self, word):
        p = self.root
        for c in word:            
            if c not in p: 
                p[c] = {}
            ### NOTE THIS
            p = p[c]
        ### NOTE HERE
        p['#'] = True  # ‘#’ is a key indicating word bounday
 
    def search(self, word):
        node = self.find(word)
        return node is not None and '#' in node   # NOTE     
 
    def startsWith(self, prefix):
        return self.find(prefix) is not None  # NOTE 
    
    ### NOTE : remember to implement this help fuunc
    def find(self, prefix):
        p = self.root
        for c in prefix:            
            if c not in p: 
                return None
            # for validating if "search to the end" (check '#' in the node or not)    
            p = p[c]
        return p

# V1
# IDEA : USE dict AS data structure (# TrieNode: is dict, or hashmap)
# https://leetcode.com/problems/implement-trie-prefix-tree/discuss/633007/25-lines-python-use-50-less-code-than-c%2B%2B-should-I-change-to-python
class Trie(object):            
    def __init__(self):
        self.root = {} # TrieNode: is dict, or hashmap       
 
    def insert(self, word):
        p = self.root
        for c in word:            
            if c not in p: 
                p[c] = {}
            p = p[c]
        ### NOTE HERE
        p['#'] = True  # ‘#’ is a key indicating word bounday
 
    def search(self, word):
        node = self.find(word)
        return node is not None and '#' in node   # NOTE     
 
    def startsWith(self, prefix):
        return self.find(prefix) is not None  # NOTE 
    
    def find(self, prefix):
        p = self.root
        for c in prefix:            
            if c not in p: 
                return None
            p = p[c]
        return p

# V1 
# https://blog.csdn.net/fuxuemingzhu/article/details/79388432
class Node(object):
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isword = False
        
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for w in word:
            current = current.children[w]
        current.isword = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for w in word:
            current = current.children.get(w)
            if current == None:
                return False
        return current.isword

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for w in prefix:
            current = current.children.get(w)
            if current == None:
                return False
        return True        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# V1'
# https://www.jiuzhang.com/solution/implement-trie-prefix-tree/#tag-highlight-lang-python
class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    
class Trie:
    
    def __init__(self):
        self.root = TrieNode()

    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        
        node.is_word = True

    """
    return the node in the trie if exists 
    """
    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None
        return node
        
    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        node = self.find(word)
        return node is not None and node.is_word

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        return self.find(prefix) is not None

# V1''
# https://www.jiuzhang.com/solution/implement-trie-prefix-tree/#tag-highlight-lang-python
class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    
class Trie:
    
    def __init__(self):
        self.root = TrieNode()

    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        
        node.is_word = True

    """
    return the node in the trie if exists 
    """
    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None
        return node
        
    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        node = self.find(word)
        return node is not None and node.is_word

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        return self.find(prefix) is not None

# V2 
# Time:  O(n), per operation
# Space: O(1)
class TrieNode(object):
    # Initialize your data structure here.
    def __init__(self):
        self.is_string = False
        self.leaves = {}

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        cur = self.root
        for c in word:
            if not c in cur.leaves:
                cur.leaves[c] = TrieNode()
            cur = cur.leaves[c]
        cur.is_string = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node = self.childSearch(word)
        if node:
            return node.is_string
        return False

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        return self.childSearch(prefix) is not None

    def childSearch(self, word):
        cur = self.root
        for c in word:
            if c in cur.leaves:
                cur = cur.leaves[c]
            else:
                return None
        return cur