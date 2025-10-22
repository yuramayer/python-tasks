# Reverse List

Given the head of a singly linked list. Reverse it & return

The func reverseList should do it

Refer to the ListNode class

Time complexity = O(n) & space complexity = O(1)

> Let's go through the list from beginning & the end
[1, 2, 5, 9, 0, -1, 7]

1 changes with 7
2 changes with -1
5 changes with 0
9 changews with 9? => stays the same

so lst[0] = lst[-1]
lst[1] = lst[-2]
lst[2] = lst[-3]

=> lst[n] = lst[-1-n]

till the middle!
if len(lst) = 1 => nothing changes
if len(lst) = 2 => changes 1 & -1
if len(lst) = 3 => just as prev
if len(lst) = 4 => changes 1 & -1, 2 & -2
etc

it means we are moving from the beginning and to the end, & change the flags. Let's realize it with python