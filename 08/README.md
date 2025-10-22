# Merge Intervals

Merge Intervals. An interval is a representation of a range of values along a number line. For example, [1,3] represents all numbers between 1 and 3, inclusive. Given a collection of intervals, the task is to merge all overlapping intervals.

For example, consider the intervals [1,3],[2,6],[8,10],[15,18]. The function should return merged intervals where overlapping intervals are combined. In this case, intervals [1,3] and [2,6] overlap, so they should be merged into [1,6]

> Let's think

First let's sort them by start. Without it it's dead end.

Then let's iterate through them. Each time with the next pair we should check:

- if the start is equal or less then our prev end? We're remembering our prev_start and prev_end

If it is, we create new pair of prev_start and prev_end. prev_start is the same, and prev_end is new end. If not, we save our prev pair to the list, and update it with current.

So first we have O(n log n) with sorting, and then O(n) with iterating

let's code