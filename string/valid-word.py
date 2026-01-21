class Solution:
    def isValid(self, word: str) -> bool:
        word = word.lower()
        if len(word) < 3:
            return False
        
        vowel = 0
        consonant = 0
        vowel_list = ['a', 'e', 'i', 'o', 'u']
        sign_list = ['@', '#', '$']
        digit_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        for ch in word:
            if ch in vowel_list:
                vowel += 1
            
            elif ch in sign_list:
                return False
            
            elif ch not in (vowel_list and sign_list and digit_list):
                consonant += 1

        if vowel == 0:
            return False
        
        elif consonant == 0:
            return False
        
        return True