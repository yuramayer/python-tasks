def merge_intervals(
        intervals: list[list[int]]
        ) -> list[list[int]]:
    """Merges intervals in the list & returns the list"""
    if not intervals:
        return []
    if len(intervals) == 1:
        return intervals
    intervals.sort(key=lambda x: x[0])

    prev_start, prev_end = intervals[0]
    result = []
    for pair in intervals[1:]:
        start, end = pair
        if start <= prev_end:
            prev_end = max(prev_end, end)
        else:
            result.append([prev_start, prev_end])
            prev_start, prev_end = start, end
    result.append([prev_start, prev_end])
    return result