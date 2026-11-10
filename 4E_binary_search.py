'''
Given a sorted array of distinct integers and a target value, return the index of the target or -1 if not found.

Example 1

Input:
nums = [1, 2, 3, 4, 5]
target = 3

Output:
2

Explanation:

Initialize low = 0, high = 4. Compute mid = (0 + 4) // 2 = 2. nums[2] = 3 matches target, so return 2.

Example 2

Input:

nums = [2, 4, 6, 8, 10, 12, 14, 16]
target = 16
Output:

7
'''
def binarySearch(nums:list, target:int) -> int:
    nums.sort()
    low_idx = 0
    high_idx = len(nums) - 1
    
    while low_idx <= high_idx:
        mid_idx = (low_idx + high_idx) // 2
        
        if(nums[mid_idx] == target):
            return mid_idx
        
        if target > nums[mid_idx]:
            low_idx = mid_idx+1
        else:
            high_idx=mid_idx-1
            
    return -1