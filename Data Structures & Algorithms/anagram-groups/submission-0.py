class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for string in strs:
            frequency_array = [0]*26
            for char in string:
                frequency_array[ord(char)-ord('a')] +=1
            freq_key = tuple(frequency_array)
            if freq_key in hashmap:
                hashmap[freq_key].append(string)
            else:
                hashmap[freq_key] = [string]
            
        return list(hashmap.values())


                
