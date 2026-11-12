'''
Maximum Number of Non-Overlapping Intervals

Given an array of intervals where each interval has a start and end time, return the maximum number of non-overlapping intervals.

Example 1

Input:
meetings = [[1, 2], [2, 3], [3, 4], [1, 3]]

Output:
3

Explanation:

Step 1: Sort meetings by end time → [[1,2],[2,3],[1,3],[3,4]].
Step 2: Select [1,2] (count=1, last_end=2).
Step 3: [2,3] has start 2 ≥ 2, select (count=2, last_end=3).
Step 4: [1,3] start 1 < 3, skip.
Step 5: [3,4] start 3 ≥ 3, select (count=3). Result = 3.

Example 2

Input:
meetings = [[0, 5], [0, 1], [1, 2], [2, 3], [3, 5], [4, 6]]

Output:
4

Explanation:
Step 1: Sort by end time → [[0,1],[1,2],[2,3],[3,5],[0,5],[4,6]].
Step 2: Select [0,1] (count=1, end=1).
Step 3: [1,2] (count=2, end=2).
Step 4: [2,3] (count=3, end=3).
Step 5: [3,5] (count=4, end=5). Skip [0,5] and [4,6] because their start times are before last_end=5. Result = 4.
'''
def maximizeNonOverlappingMeetings(meetings:list[list[int]])->int:
    meetings.sort(key=lambda x:x[-1]) #sort by end time
    prev_end = 0
    non_overlap_count = 0
    for idx, duration in enumerate(meetings):
        if prev_end <= duration[0]:
            non_overlap_count+=1
            prev_end = duration[1]
    return non_overlap_count