'''
Find First Occurrence

Given a sorted array of integers that may contain duplicates, return the index of the first occurrence of a target value or -1 if not found.

Example

Input:
nums = [1, 2, 3, 4, 5]
target = 3

Output:
2

Explanation:

We perform binary search on [1,2,3,4,5].

low=0, high=4 → mid=2 → nums[2]=3 equals target. Record result=2, then search left half.
Update high=mid-1=1. Now low=0, high=1 → mid=0 → nums[0]=1 < target, so move low to mid+1=1.
low=1, high=1 → mid=1 → nums[1]=2 < target, so move low to mid+1=2.
Now low(2)>high(1), terminate. The first occurrence found is at index 2.
'''

def findFirstOccurrence(nums: list, target: int) -> int:
    nums.sort()
    low_idx = 0
    high_idx = len(nums) - 1
    
    first_occurence = -1
    while low_idx <= high_idx:
        mid_idx = (low_idx + high_idx) // 2 
        
        if nums[mid_idx] == target:
            if first_occurence < 0:
                first_occurence = mid_idx 
            if 0 <= mid_idx < first_occurence: 
                first_occurence = mid_idx
        
        if target > nums[mid_idx]:
            low_idx = mid_idx+1
        else:
            high_idx = mid_idx-1
        
    return first_occurence