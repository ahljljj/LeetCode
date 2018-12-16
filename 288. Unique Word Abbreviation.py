'''
288. Unique Word Abbreviation

An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
     ↓
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
     ↓   ↓    ↓    ↓  ↓
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
     ↓   ↓    ↓
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example:

Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true

'''

# hashtable and set

'''

The logic in isUnique(word) is tricky. You need to consider the following cases:

Does the word's abbreviation exists in the dictionary? If not, then it must be unique.
If above is yes, then it can only be unique if the grouping of the abbreviation contains no other words except word.
'''
class ValidWordAbbr:

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.map = {}
        self.dictionary = set(dictionary)
        for word in self.dictionary:
            word = self.encode(word)
            self.map[word] = self.map.get(word, 0) + 1

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word in self.dictionary:
            word = self.encode(word)
            if self.map[word] > 1:
                return False
        elif self.encode(word) in self.map:
            return False
        return True

    def encode(self, word):
        if len(word) < 3:
            return word
        return word[0] + str(len(word) - 2) + word[-1]

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)

# cpp, rewrite

'''

class ValidWordAbbr {
    unordered_set<string> dict;
    unordered_map<string, int> map;
public:
    ValidWordAbbr(vector<string> dictionary) {
        for (auto word: dictionary) dict.insert(word);
        for (auto word: dict) map[encode(word)] += 1;
        
    }
    
    bool isUnique(string word) {
        string pw = encode(word);
        if (dict.find(word) != dict.end()){
            if (map[pw] > 1) return false;
        }else if (map.find(pw) != map.end()) return false;
        return true;
        
    }
    string encode(string word){
        if (word.size() < 3) return word;
        return word[0] + to_string(word.size() - 2) + word[word.size() - 1];
         
    }
};

/**
 * Your ValidWordAbbr object will be instantiated and called as such:
 * ValidWordAbbr obj = new ValidWordAbbr(dictionary);
 * bool param_1 = obj.isUnique(word);
 */
'''