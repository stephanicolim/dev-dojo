'''
Check Palindrome by Filtering Non-Letters

Given a string containing letters, digits, and symbols, determine if it reads the same forwards and backwards when considering only alphabetic characters (case-insensitive).
1 = True, 0 = False
Example

Input
code = A1b2B!a
Output
1
'''

import re
def isAlphabeticPalindrome(code: str) -> bool:
    isPalindrome = False
    
    alphabets = "".join(re.findall(r'[a-zA-Z]', code)).lower()
    count_letters = len(alphabets)
    
    alphabets_reversed = alphabets[::-1].lower()
    
    if alphabets == alphabets_reversed or count_letters <= 1:  
        isPalindrome = True
            
    return isPalindrome