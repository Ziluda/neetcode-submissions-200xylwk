class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap char_count list to list of anagrams
        result = defaultdict(list) # don't have to deal with the edge case of keys not existing for an anagram group 

        # go through each element in the list of strings
        for s in strs:
            count = [0] * 26 # one placeholder counter for each alphabet
            
            # go through each character in a string element
            for char in s:
                count[ord(char)-ord("a")]+=1
        
            # add the anagram group as a tuple key into the result dictionary along with the current string as its value
            result[tuple(count)].append(s)
        
        return list(result.values())