class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        start_counter = 0
        anagram_final = []
        while strs:  # Iterate while there are still items in the list
            word = strs[0]  # Get the first word
            anagram_list = [word]  # Start a list of anagrams with the first word
            for comparative_word in strs[1:]:  # Compare against the rest of the list
                if len(word) != len(comparative_word):
                    continue  # If lengths don't match, it's not an anagram
                
                are_anagrams = True 

                for character in word:  # Check character frequencies
                    word_character_count = word.count(character)
                    comp_word_character_count = comparative_word.count(character)
                    if word_character_count != comp_word_character_count:
                        are_anagrams = False
                        break

                if are_anagrams:  
                    anagram_list.append(comparative_word)
            
            anagram_final.append(anagram_list)

            # Remove all anagrams of the current word from `strs`
            for item in anagram_list:
                strs.remove(item)

        return anagram_final
        
            

                
                 
                    
                        
