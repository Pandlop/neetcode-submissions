class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}

        i=0
    
        res = 0
        max_val = 0

        for j in range(len(s)):
            if s[j] not in freq:
                freq[s[j]] = 1    
            else:
                freq[s[j]]+=1

            max_val = max(max_val, freq[s[j]])
            
            while (j - i + 1) - max_val > k:
                freq[s[i]] -= 1
                i += 1

            res = max(res, j - i + 1)

        return res


# XY, repl=2-1=1, long=2
# XYY, repl=3-2=1, long=3
#XYYX, repl=4-2=2, long=4

# AA, repl=2-2=0 - 2

# AAA, repl=3-3=0 - 3
# AAAB, repl=4-3=1 - 4
# AAABA, repl=5-4=1 - 5
# AAABAB, repl=6-4=2>1
#  AABAB, repl=5-3=2>1
#   ABAB, repl=4-2-2>1
#    BAB, repl=3-2=1, 5
#    BABB, repl=4-1=3>1
#     ABB, repl=3-2=1, 5
#     ABB, repl=4-1=3>1
