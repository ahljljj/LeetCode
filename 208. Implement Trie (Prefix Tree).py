"""
208. Implement Trie (Prefix Tree)


Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.


"""


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.endofword = False


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for s in word:
            if s not in curr.children:
                curr.children[s] = TrieNode()
            curr = curr.children[s]
        curr.endofword = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for s in word:
            if s not in curr.children:
                return False
            curr = curr.children[s]
        return curr.endofword

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for s in prefix:
            if s not in curr.children:
                return False
            curr = curr.children[s]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

















# cpp, rewrite

'''
struct TrieNode{
    unordered_map<char, TrieNode*> kids;
    bool endOfWord;
    TrieNode(bool b = false){
        endOfWord = b;
    }
};



class Trie {
    TrieNode *root;
public:
    /** Initialize your data structure here. */
    Trie() {
        root = new TrieNode();
    }
    ~Trie(){
        destroy(root);
    }
    void destroy(TrieNode *node){
        for (auto &p: node->kids){
            destroy(p.second);
        }
        delete node;
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        TrieNode *curr = root;
        for (char &s: word){
            if (curr->kids.find(s) == curr->kids.end()){
                curr->kids[s] = new TrieNode();
            }
            curr = curr->kids[s];
        }
        curr->endOfWord = true;
        
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        TrieNode *curr = root;
        for (char &s: word){
            if (curr->kids.find(s) == curr->kids.end()) return false;
            curr = curr->kids[s];
        }
        return curr->endOfWord;
        
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        TrieNode *curr = root;
        for (char &s: prefix){
            if (curr->kids.find(s) == curr->kids.end()) return false;
            curr = curr->kids[s];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * bool param_2 = obj.search(word);
 * bool param_3 = obj.startsWith(prefix);
 */
'''


# 2020/06/04, prefix/hash table


'''
Runtime: 180 ms, faster than 70.05% of Python3 online submissions for Implement Trie (Prefix Tree).
Memory Usage: 31.2 MB, less than 11.11% of Python3 online submissions for Implement Trie (Prefix Tree).
'''


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.is_word = True

    def find(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w, None)
            if not node: return None
        return node

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.find(word)
        return node and node.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.find(prefix)