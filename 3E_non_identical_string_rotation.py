'''
Check for Non-Identical String Rotation

Given two strings s1 and s2, return 1 if s2 is a rotation of s1 but not identical to s1, otherwise return 0.

Example

Input:
s1 = abcde
s2 = cdeab

Output:
True
'''

def isNonTrivialRotation(s1: str, s2:str) -> bool:
    s1, s2 = s1.lower(), s2.lower()
    if len(s1) == len(s2) and s1!=s2 and s1 in (s2+s2):
        return True
    return False
