class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []
        elif len(strs) == 1:
            return [strs]

        anagrams = {}
        for s in strs:
            new_s = "".join(sorted(s))
            if new_s in anagrams:
                anagrams[new_s].append(s)
            else:
                anagrams[new_s] = [s]
        return list(anagrams.values())

            






        