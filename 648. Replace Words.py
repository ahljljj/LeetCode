'''

648. Replace Words

In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.



Example 1:

Input: dict = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"


Constraints:

The input will only have lower-case letters.
1 <= dict.length <= 1000
1 <= dict[i].length <= 100
1 <= sentence words number <= 1000
1 <= sentence words length <= 1000
Accepted
52,112
Submissions
93,251

'''


# 2020/06/05, brute force???


'''
Runtime: 208 ms, faster than 28.96% of Python3 online submissions for Replace Words.
Memory Usage: 18.5 MB, less than 68.67% of Python3 online submissions for Replace Words.
'''


class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        sentence = sentence.split()
        dict = set(dict)
        for i, word in enumerate(sentence):
            for j in range(len(word)):
                if word[:j + 1] in dict:
                    sentence[i] = word[:j + 1]
                    break
        return " ".join(sentence)

# 2020/06/05, trie, too smart

'''
Runtime: 112 ms, faster than 75.66% of Python3 online submissions for Replace Words.
Memory Usage: 35.3 MB, less than 27.31% of Python3 online submissions for Replace Words.
'''


class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dict:
            trie.insert(word)
        sentence = sentence.split(" ")
        for i, word in enumerate(sentence):
            sentence[i] = trie.find_prefix(word)
        return " ".join(sentence)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def find_prefix(self, word):
        node = self.root
        prefix = ""
        for c in word:
            node = node.children.get(c)
            if not node: break
            prefix += c
            if node.is_word: return prefix
        return word
