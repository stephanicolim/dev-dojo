'''
Validate Properly Nested Brackets

Given a string, check if all brackets ('()', '{}', '[]') are properly matched and nested. Return 1 if valid, otherwise return 0.

Input:
[()] {}

Output:
True

Input:
(}}}

Output:
False
'''

import re

def areBracketsProperlyMatched(code_snippet:str)->bool:
    bracket_dict = {"(":")", "[":"]", "{":"}"}
    code_brackets = re.findall(r"[(){}\[\]]", code_snippet)
    
    stack = []
    for code_bracket in code_brackets:
        stack.append(code_bracket)
        if len(stack) > 1 and stack[-2] in bracket_dict.keys():
            if bracket_dict[stack[-2]] == stack[-1]:
                stack.pop()
                stack.pop()
    return len(stack) == 0