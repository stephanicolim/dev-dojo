'''
Min-Tracking Stack Implementation

Implement a stack that supports push, pop, top, and getMin operations in O(1) time, where getMin returns the minimum element.

Input
n = 10
operations = ['push 2', 'push 0', 'push 3', 'push 0', 'getMin', 'pop', 'getMin', 'pop', 'top', 'getMin']

Output
[0,0,0,0]
Explanation

- push 2 → stack = [2]
- push 0 → stack = [2,0]
- push 3 → stack = [2,0,3]
- push 0 → stack = [2,0,3,0]
- getMin → returns 0
- pop → removes 0, stack = [2,0,3]
- getMin → returns 0
- pop → removes 3, stack = [2,0]
- top → returns 0 
- getMin → returns 0
'''

def processCouponStackOperations(operations: list[str]) -> list[int]:
    stack = []
    result = []
    for o in operations:
        if " " in o:
            o, num = o.split(" ")
            num = int(num)
        if o == "getMin":
            result.append(min(stack))
        elif o == "pop":
            stack.pop()
        elif o == "top":
            result.append(stack[-1])                
        elif o == "push":
            stack.append(num)
    return result