from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)
        count_t = Counter(t)
        
        for letter in count_t:
            if count_t[letter] != count_s.get(letter, 0):
                return letter

