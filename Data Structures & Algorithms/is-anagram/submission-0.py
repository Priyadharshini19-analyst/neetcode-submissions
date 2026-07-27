class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
         if len(s) != len(t):     # different lengths can't be anagrams
            return False
         counts = {}
         for ch in s:
            counts[ch] = counts.get(ch, 0) + 1   # tally each letter in s
         for ch in t:
            if ch not in counts:
                return False       # letter in t that s never had
            counts[ch] -= 1
            if counts[ch] == 0:
                del counts[ch]
         return len(counts) == 0    # empty means perfect match
        