class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        index = {}
        result = []

        for word in strs:
            char_index = [0] * 26
            for char in word:
                char_index[ord(char)-ord('a')] += 1
                
            index.setdefault(tuple(char_index),[]).append(word)


        return list(index.values())




        


        